import React, { useState } from "react";
import { Link } from "react-router-dom";
import {
  FaHome,
  FaVideo,
  FaDatabase,
  FaComments,
  FaUserPlus,
} from "react-icons/fa";
import "./assistant.css";

const Assistant = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleAsk = async () => {
    if (!question.trim()) return;
    try {
      const response = await fetch("http://localhost:5000/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      const data = await response.json();
      setAnswer(data.answer || "No answer received.");
    } catch (error) {
      setAnswer("Error connecting to backend.");
      console.error("Error:", error);
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
          <Link to="/registerpage" className="menu-item">
            <FaUserPlus className="icon" />
            <span>Register</span>
          </Link>
          <Link to="/livestream" className="menu-item">
            <FaVideo className="icon" />
            <span>Livestream</span>
          </Link>
          <Link to="/assistant" className="menu-item active">
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

      <div className="assistant-container">
        <h1 className="title">Face Recognition Assistant</h1>
        <ul className="sub-list">
          <li>“Who was the last person registered?”</li>
          <li>“When was John added?”</li>
          <li>“How many faces are stored?”</li>
        </ul>

        <div className="input-group">
          <input
            type="text"
            placeholder="Ask your question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleAsk()}
          />
          <button onClick={handleAsk}>Ask</button>
        </div>
        {answer && (
          <div className="answer">
            <strong>Answer:</strong> {answer}
          </div>
        )}
      </div>
    </div>
  );
};

export default Assistant;
