import React, { useRef, useState, useEffect } from "react";
import {
  FaHome,
  FaDatabase,
  FaVideo,
  FaComments,
  FaUserPlus,
} from "react-icons/fa";
import "./registerpage.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Link } from "react-router-dom";

function Registerpage() {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [capturedImage, setCapturedImage] = useState(null);
  const [cameraOn, setCameraOn] = useState(false);
  const [name, setName] = useState("");

  const startCamera = () => {
    navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
      const video = videoRef.current;
      video.srcObject = stream;
      video.play();
      setCameraOn(true);
    });
  };

  const captureImage = () => {
    const video = videoRef.current;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const dataUrl = canvas.toDataURL("image/png");
    setCapturedImage(dataUrl);
    video.srcObject.getTracks().forEach((track) => track.stop());
    setCameraOn(false);
  };

  const retakeImage = () => {
    setCapturedImage(null);
    startCamera();
  };

  const submitData = async () => {
    if (!name || !capturedImage) {
      alert("Please enter your name and capture a photo!");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: name,
          image: capturedImage,
        }),
      });

      const result = await response.json();
      alert(result.message);
      setCapturedImage(null);
      setName("");
    } catch (error) {
      console.error("Error submitting data:", error);
      alert("Failed to register face. Try again.");
    }
  };

  return (
    <div className="app-container">
      <div className="sidebar">
        <div className="sidebar-header">
          <h2>FaceVerse AI</h2>
        </div>

        <div className="sidebar-menu">
          <Link to="/" className="menu-item">
            <FaHome className="icon" />
            <span>Home</span>
          </Link>
          <Link to="/registerpage" className="menu-item active">
            <FaUserPlus className="icon" />
            <span>Register</span>
          </Link>
          <Link to="/livestream" className="menu-item ">
            <FaVideo className="icon" />
            <span>Livestream</span>
          </Link>
          <Link to="/assistant" className="menu-item ">
            <FaComments className="icon" />
            <span>Q-A Assistant</span>
          </Link>
          <Link to="/databasepage" className="menu-item">
            <FaDatabase className="icon" />
            <span>Database</span>
          </Link>
        </div>

        <div className="sidebar-footer">
          <span className="user-name">POORANI</span>
        </div>
      </div>

      <div className="main-content">
        <div className="registration-container">
          <h3>Face Registration</h3>
          <p>Register new faces for recognition system</p>

          <label>Full Name</label>
          <input
            type="text"
            placeholder="Enter full name"
            className="form-control"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />

          <label>Capture Photo</label>
          <div className="camera-section">
            {!capturedImage && (
              <>
                <video
                  ref={videoRef}
                  className="camera-preview"
                  autoPlay
                  muted
                  playsInline
                />
                <canvas
                  ref={canvasRef}
                  width="300"
                  height="300"
                  style={{ display: "none" }}
                />
              </>
            )}
            {capturedImage && (
              <img
                src={capturedImage}
                alt="Captured"
                className="captured-image"
              />
            )}
          </div>

          {!capturedImage && !cameraOn && (
            <button className="btn btn-info" onClick={startCamera}>
              📷 Start Camera
            </button>
          )}

          {cameraOn && (
            <button className="btn btn-success" onClick={captureImage}>
              ✅ Capture Image
            </button>
          )}

          {capturedImage && (
            <button className="btn btn-warning" onClick={retakeImage}>
              🔁 Retake
            </button>
          )}

          <button className="btn btn-primary w-100 mt-3" onClick={submitData}>
            Register Face
          </button>
        </div>
      </div>
    </div>
  );
}

export default Registerpage;
