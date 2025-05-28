import React, { useEffect, useState } from "react";
import "./databasepage.css";
import {
  FaHome,
  FaUserPlus,
  FaComments,
  FaDatabase,
  FaVideo,
} from "react-icons/fa";
import { Link } from "react-router-dom";

function DatabasePage() {
  const [faces, setFaces] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/faces")
      .then((res) => res.json())
      .then((data) => setFaces(data))
      .catch((err) => console.error("Error fetching faces", err));
  }, []);

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

          <Link to="/registerpage" className="menu-item">
            <FaUserPlus className="icon" />
            <span>Register</span>
          </Link>
          <Link to="/livestream" className="menu-item">
            <FaVideo className="icon" />
            <span>Livestream</span>
          </Link>
          <Link to="/assistant" className="menu-item">
            <FaComments className="icon" />
            <span>Q-A Assistant</span>
          </Link>
          <Link to="/databasepage" className="menu-item active">
            <FaDatabase className="icon" />
            <span>Database</span>
          </Link>
        </div>

        <div className="sidebar-footer">
          <span className="user-name">POORANI</span>
        </div>
      </div>

      <div className="database-container">
        <h2>📦 Registered Face Database</h2>
        <div className="face-grid">
          {faces.map((face) => (
            <div key={face.id} className="face-card">
              <img
                src={`http://localhost:5000/registered_faces/${face.filename}`}
                alt={face.name}
                className="face-img"
              />
              <div className="face-details">
                <h5>{face.name}</h5>
                <p className="timestamp">{face.timestamp}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default DatabasePage;
