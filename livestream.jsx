import React, { useEffect } from "react";
import { Link } from "react-router-dom";
import "./livestream.css";
import {
  FaHome,
  FaDatabase,
  FaVideo,
  FaComments,
  FaUserPlus,
} from "react-icons/fa";

const Livestream = () => {
  useEffect(() => {
    fetch("http://localhost:5000/start_feed", { method: "POST" });

    return () => {
      fetch("http://localhost:5000/stop_feed", { method: "POST" });
    };
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
          <Link to="/livestream" className="menu-item active">
            <FaVideo className="icon" />
            <span>Livestream</span>
          </Link>
          <Link to="/assistant" className="menu-item">
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

      <div className="livestream-content">
        <h2>Live Face Recognition</h2>
        <img
          src="http://localhost:5000/video_feed"
          alt="Live Stream"
          style={{
            width: "100%",
            maxWidth: "720px",
            borderRadius: "8px",
            border: "2px solid #ccc",
          }}
        />
      </div>
    </div>
  );
};

export default Livestream;
