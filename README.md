# 📌 Face Recognition Platform

An integrated face recognition system with live streaming, user face registration, and intelligent chat-based assistance. Built using **React**, **Flask**, **OpenCV**, and **face_recognition**, this platform allows real-time face detection and identification in both webcam and uploaded images, with a supporting knowledge assistant powered by **LangChain RAG**.

---

## 🚀 Features

- 🔐 **Face Registration**  
  Upload and register a user's face with name and image stored in SQLite.

- 🎥 **Live Face Recognition**  
  Detect and recognize multiple faces from a webcam stream using `Haar Cascades` and `face_recognition`.

- 📁 **Face Database Viewer**  
  View all registered faces and associated metadata in a clean dashboard.

- 🤖 **Chat-Based Assistance (RAG)**  
  Ask questions about face registration using a built-in AI assistant trained via LangChain and FAISS over your documents.

- 🖼️ **Image Upload Recognition**  
  Upload an image and detect any registered faces within it.

- 🔗 **Backend-Frontend Integration**  
  React frontend integrated with Flask API for live detection and communication.

---

## 🛠️ Tech Stack

| Layer         | Technology                      |
|--------------|----------------------------------|
| Frontend     | React JS, HTML, CSS              |
| Backend      | Flask (Python), face_recognition |
| Database     | SQLite3                          |
| Face Detection | Haar Cascades (OpenCV)         |
| Face Recognition | dlib + face_recognition      |
| AI Assistant | LangChain, FAISS, OpenAI         |

---

## 📦 Folder Structure
![image](https://github.com/user-attachments/assets/2fd013ce-e4bf-4da7-b031-26ae84b992cf)



## 📦 Architectural Diagram

![image](https://github.com/user-attachments/assets/fee32754-6571-438d-a5bb-bebfba235e91)


![image](https://github.com/user-attachments/assets/238b902e-0a72-4c97-a279-d69cc20e0d75)


## 🏠 Home Page
Introduction about the application

Navigation sidebar with routes to each page

![image](https://github.com/user-attachments/assets/aab2ae0f-1edd-4a2f-87f9-1d63339e8a5e)

## 📝 Face Registration Page (/registerpage)
Upload face image and assign name

Saves image to registered_faces/ and metadata in SQLite

Also updates the face_registration_guide.txt used by the assistant

![image](https://github.com/user-attachments/assets/167faf64-d67f-4c35-bc43-997641d7329d)

## 🎥 Live Face Recognition (/livestream)
Starts webcam live feed

Detects faces using Haar Cascades

Recognizes with face_recognition and overlays name boxes


## 🧠 Q&A Assistant (/assistant)
Ask questions about face registration, system usage, or steps

Powered by LangChain Retrieval-Augmented Generation (RAG)

Context from your face_registration_guide.txt

![image](https://github.com/user-attachments/assets/074a4fc6-f368-4c80-b35f-2818ad7822b7)

## 🗃️ Face Database Page (/databasepage)
Lists all registered users

Displays image, name, and database info

Allows manual delete from UI (optional)



![image](https://github.com/user-attachments/assets/747502d8-1aaf-415b-b226-f22067b5c442)
