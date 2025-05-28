# import cv2
# import face_recognition
# import os
# import numpy as np

# # Load Haar Cascade
# haar_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
# face_cascade = cv2.CascadeClassifier(haar_path)

# # Load registered faces
# def load_known_faces(path='registered_faces'):
#     known_encodings = []
#     known_names = []
#     for file in os.listdir(path):
#         if file.endswith('.png') or file.endswith('.jpg'):
#             img = face_recognition.load_image_file(os.path.join(path, file))
#             encodings = face_recognition.face_encodings(img)
#             if encodings:
#                 known_encodings.append(encodings[0])
#                 name = file.split("_")[0]
#                 known_names.append(name)
#     return known_encodings, known_names

# known_encodings, known_names = load_known_faces()

# # Open webcam
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert to grayscale for Haar
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # Detect faces using Haar
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#     # Convert frame to RGB for face_recognition
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Encode faces
#     face_encodings = face_recognition.face_encodings(rgb_frame)

#     for (x, y, w, h), face_encoding in zip(faces, face_encodings):
#         matches = face_recognition.compare_faces(known_encodings, face_encoding)
#         name = "Unknown"

#         face_distances = face_recognition.face_distance(known_encodings, face_encoding)
#         if matches:
#             best_match_index = np.argmin(face_distances)
#             if matches[best_match_index]:
#                 name = known_names[best_match_index]

#         # Draw bounding box and name
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         cv2.rectangle(frame, (x, y - 25), (x + w, y), (0, 255, 0), cv2.FILLED)
#         cv2.putText(frame, name, (x + 5, y - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

#     cv2.imshow("Live Face Recognition", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()





import face_recognition
import cv2
import os
import numpy as np

def load_known_faces(path='registered_faces'):
    known_encodings, known_names = [], []
    for file in os.listdir(path):
        if file.endswith(('.jpg', '.jpeg', '.png')):
            image = face_recognition.load_image_file(os.path.join(path, file))
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(file.split('_')[0])
    return known_encodings, known_names

known_face_encodings, known_face_names = load_known_faces()
video_capture = None

def generate_frames():
    global video_capture
    video_capture = cv2.VideoCapture(0)
    while True:
        success, frame = video_capture.read()
        if not success:
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            if matches:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 1)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def release_camera():
    global video_capture
    if video_capture:
        video_capture.release()
        video_capture = None
