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



