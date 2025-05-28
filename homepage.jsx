import React from "react";
import {
  FaHome,
  FaComments,
  FaVideo,
  FaDatabase,
  FaUserPlus,
} 
from "react-icons/fa"; 
import "./homepage.css";
import "bootstrap/dist/css/bootstrap.min.css"; 
import { Link } from "react-router-dom";

function Homepage() {
  // Print function
  const myFunction = () => {
    window.print();
  };

  return (
    <div className="app-container">
      {/* Sidebar Section */}
      <div className="sidebar">
        <div className="sidebar-header">
          <h2>FaceVerse AI</h2>
        </div>

        <div className="sidebar-menu">
          <Link to="/" className="menu-item active">
            <FaHome className="icon" />
            <span>Home</span>
          </Link>

          <Link to="/registerpage" className="menu-item">
            <FaUserPlus className="icon" />
            <span>Register</span>
          </Link>

          <Link to="/livestream" className="menu-item ">
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

      <div className="home-container">
        <div className="home-content">
          <h1>
            Welcome to <span className="highlight">FaceVerse AI</span>
          </h1>
          <p className="intro">
            A smart, secure, and seamless system for real-time face recognition
            and user management.
          </p>

          <div className="features">
            <p>This platform enables you to:</p>
            <ul>
              <li>
                <strong>Register:</strong> Add new users with face image and
                details.
              </li>
              <li>
                <strong>Livestream:</strong> Detect and recognize faces in
                real-time using your camera.
              </li>
              <li>
                <strong>Q-A Assistant:</strong> Ask questions related to face
                registration and get instant help.
              </li>
              <li>
                <strong>Database:</strong> View, search, and manage the
                registered user data.
              </li>
            </ul>
          </div>

          <p className="cta">
            🚀 Click on any feature in the sidebar to get started!
          </p>
        </div>
      </div>
    </div>
  );
}

export default Homepage;
