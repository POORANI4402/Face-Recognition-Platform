
from flask import Flask, request, jsonify, send_from_directory, Response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import base64
import os
import cv2
import face_recognition
import numpy as np
from datetime import datetime, timedelta
import re

from rag_chat import setup_rag
conversation_chain = None
rag_data_path = "data/face_registration_guide.txt"

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///faces.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
UPLOAD_FOLDER = 'registered_faces'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db = SQLAlchemy(app)

class Face(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    filename = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_]', '_', name)

haar_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_path)

def load_known_faces(path='registered_faces'):
    known_encodings = []
    known_names = []
    for file in os.listdir(path):
        if file.endswith(('.png', '.jpg', '.jpeg')):
            image = face_recognition.load_image_file(os.path.join(path, file))
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                name = file.split('_')[0]
                known_names.append(name)
    return known_encodings, known_names

known_encodings, known_names = load_known_faces()

@app.route('/')
def home():
    return "Flask backend with face recognition is running."

@app.route('/register', methods=['POST'])
def register_face():
    data = request.get_json()
    name = data.get('name')
    image_data = data.get('image')

    if not name or not image_data:
        return jsonify({"message": "Missing name or image data"}), 400

    try:
        if ',' in image_data:
            image_data = image_data.split(",")[1]

        image_bytes = base64.b64decode(image_data)
        timestamp = datetime.now()
        timestamp_str = timestamp.strftime("%Y%m%d%H%M%S")
        safe_name = sanitize_filename(name)
        filename = f"{safe_name}_{timestamp_str}.png"
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        with open(filepath, "wb") as f:
            f.write(image_bytes)

        new_face = Face(name=name, filename=filename, timestamp=timestamp)
        db.session.add(new_face)
        db.session.commit()

        with open(rag_data_path, "a") as f:
            f.write(f"Name: {name}\nTimestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\nFilename: {filename}\n\n")

        global known_encodings, known_names
        known_encodings, known_names = load_known_faces()

        return jsonify({"message": f"{name}'s face registered successfully.", "filename": filename}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "Failed to process image."}), 500

@app.route('/faces', methods=['GET'])
def get_all_faces():
    faces = Face.query.order_by(Face.timestamp.desc()).all()
    results = [{
        "id": face.id,
        "name": face.name,
        "filename": face.filename,
        "timestamp": face.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    } for face in faces]
    return jsonify(results), 200

@app.route('/registered_faces/<filename>')
def serve_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/recognize', methods=['POST'])
def recognize_faces_from_image():
    data = request.get_json()
    image_data = data.get("image")

    if not image_data or ',' not in image_data:
        return jsonify({"error": "Invalid image data"}), 400

    image_data = image_data.split(",")[1]
    image_bytes = base64.b64decode(image_data)
    np_arr = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_encodings = face_recognition.face_encodings(rgb_frame)

    faces = []
    for (x, y, w, h), face_encoding in zip(detected_faces, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        if matches:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]

        faces.append({
            "top": y,
            "right": x + w,
            "bottom": y + h,
            "left": x,
            "name": name
        })

    return jsonify({"faces": faces})

# ---------- LIVE VIDEO STREAMING ----------
camera = None

def generate_frames():
    global camera
    if camera is None:
        camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb)

        for (x, y, w, h), encoding in zip(faces, encodings):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_encodings, encoding)
            if matches:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_names[best_match_index]

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y - 25), (x + w, y), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x + 5, y - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop_feed', methods=['POST'])
def stop_feed():
    global camera
    if camera:
        camera.release()
        camera = None
    return jsonify({'message': 'Camera released'})

@app.route('/query', methods=['POST'])
def query_assistant():
    data = request.get_json()
    question = data.get("question", "").lower()

    if not question:
        return jsonify({"error": "Question not provided"}), 400

    try:
        if any(kw in question for kw in ["how many", "total", "count"]):
            total = Face.query.count()
            return jsonify({"answer": f"Total registered face records: {total}"}), 200

        match = re.search(r"names? starting with ([a-z])", question)
        if match:
            letter = match.group(1).upper()
            faces = Face.query.filter(Face.name.like(f"{letter}%")).all()
            names = [face.name for face in faces]
            return jsonify({"answer": f"Names starting with {letter}: {', '.join(names) or 'None'}"})

        match = re.search(r"when did (.+?) register", question)
        if match:
            person = match.group(1).strip().capitalize()
            face = Face.query.filter(Face.name.ilike(person)).order_by(Face.timestamp.desc()).first()
            if not face:
                return jsonify({"answer": f"{person} has not been registered."})
            return jsonify({"answer": f"{person} was last registered at {face.timestamp.strftime('%Y-%m-%d %H:%M:%S')}."})

        match = re.search(r"registrations? on (\d{4}-\d{2}-\d{2})", question)
        if match:
            date_str = match.group(1)
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            next_day = date_obj + timedelta(days=1)
            count = Face.query.filter(Face.timestamp >= date_obj, Face.timestamp < next_day).count()
            return jsonify({"answer": f"Total registrations on {date_str}: {count}."})

        global conversation_chain
        if conversation_chain is None:
            conversation_chain = setup_rag(rag_data_path)
            if not conversation_chain:
                return jsonify({"error": "RAG not initialized."}), 500

        result = conversation_chain({"question": question})
        return jsonify({"answer": result["answer"]})

    except Exception as e:
        print("Query Error:", e)
        return jsonify({"error": "Something went wrong."}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

