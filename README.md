# 📌 Face Recognition Platform

An integrated face recognition system with live streaming, user face registration, and intelligent chat-based assistance. Built using **React**, **Flask**, **OpenCV**, and **face_recognition**, this platform allows real-time face detection and identification in both webcam and uploaded images, with a supporting knowledge assistant powered by **LangChain RAG**.

---

## Demo Video 
(https://drive.google.com/file/d/1Ymytddy6ONpLkWp6S_CYaOc02qpSfveV/view?usp=sharing)

## Architectue Diagram
![image](https://github.com/user-attachments/assets/3b98dfb6-ea86-4539-aae3-e4fc363d57d1)

![image](https://github.com/user-attachments/assets/3080035d-7d59-444a-8617-ecd8306264c5)


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

![image](https://github.com/user-attachments/assets/8764c173-6c0e-4abb-bd30-10d083c1c3c1)

## 🏠 Home Page
Introduction about the application

Navigation sidebar with routes to each page

![Screenshot (464)](https://github.com/user-attachments/assets/488e24e4-d447-45df-8c8e-2af9c588ca4a)

## 📝 Face Registration Page (/registerpage)
Upload face image and assign name

Saves image to registered_faces/ and metadata in SQLite

Also updates the face_registration_guide.txt used by the assistant

![Screenshot (465)](https://github.com/user-attachments/assets/7bfa213f-6f07-476f-8104-6bb2a2a0d20e)

## 🎥 Live Face Recognition (/livestream)
Starts webcam live feed

Detects faces using Haar Cascades

Recognizes with face_recognition and overlays name boxes

![image](https://github.com/user-attachments/assets/d3dd04f2-0267-43ae-998c-c940c15ce23f)

## 🧠 Q&A Assistant (/assistant)
Ask questions about face registration, system usage, or steps

Powered by LangChain Retrieval-Augmented Generation (RAG)

Context from your face_registration_guide.txt

![image](https://github.com/user-attachments/assets/fcb2d713-9d21-4fd4-88ee-c193b5cce06c)


## 🗃️ Face Database Page (/databasepage)
Lists all registered users

Displays image, name, and database info

Allows manual delete from UI (optional)

![image](https://github.com/user-attachments/assets/6f62cbe2-f927-4bdf-881d-45f89c4dfa36)


![image](https://github.com/user-attachments/assets/f0688941-7b91-4020-b1ac-c938853f8c57)


## “This project is a part of a hackathon run by https://katomaran.com ”

