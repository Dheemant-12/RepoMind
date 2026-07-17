import { useEffect, useRef, useState } from "react";
import ChatInput from "../components/ChatInput";
import MessageBubble from "../components/MessageBubble";
import { askRepository } from "../services/api";

function ChatPage() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      message:
        "👋 Welcome to RepoMind.\n\nYour repository has been indexed successfully.\nAsk me anything about the codebase.",
    },
  ]);

  const [chatHistory, setChatHistory] = useState([
    "Repository Overview",
  ]);

  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  const handleNewChat = () => {
    setChatHistory((prev) => [
      ...prev,
      `Chat ${prev.length + 1}`,
    ]);

    setMessages([
      {
        role: "assistant",
        message:
          "👋 New conversation started.\n\nWhat would you like to know about this repository?",
      },
    ]);
  };

  const handleSend = async (message) => {
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        message,
      },
      {
        role: "assistant",
        message: "🤖 RepoMind is thinking...",
      },
    ]);

    try {
      const response = await askRepository(message);

      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          role: "assistant",
          message: response.answer,
        };

        return updated;
      });
    } catch {
      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          role: "assistant",
          message:
            "Unable to reach the backend. Please ensure FastAPI is running.",
        };

        return updated;
      });
    }
  };

  return (
    <div
      style={{
        display: "flex",
        height: "100vh",
        background: "#0b1120",
        color: "white",
      }}
    >
      {/* Sidebar */}
      <div
        style={{
          width: "280px",
          background: "#111827",
          display: "flex",
          flexDirection: "column",
          padding: "20px",
          borderRight: "1px solid #1e293b",
        }}
      >
        <h2 style={{ marginBottom: "25px" }}>
          🧠 RepoMind
        </h2>

        <button
          onClick={handleNewChat}
          style={{
            padding: "14px",
            background: "#2563eb",
            color: "white",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
            marginBottom: "25px",
          }}
        >
          + New Chat
        </button>

        <h3>Recent Chats</h3>

        <div style={{ marginBottom: "30px" }}>
          {chatHistory.map((chat, index) => (
            <div
              key={index}
              style={{
                padding: "10px",
                marginTop: "8px",
                background: "#1f2937",
                borderRadius: "8px",
              }}
            >
              💬 {chat}
            </div>
          ))}
        </div>

        <h3>Repository</h3>

        <div
          style={{
            background: "#1f2937",
            padding: "15px",
            borderRadius: "10px",
            marginTop: "10px",
          }}
        >
          <strong>Flask</strong>

          <p style={{ color: "#9ca3af" }}>
            Repository indexed successfully.
          </p>
        </div>
      </div>

      {/* Chat Section */}
      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
        }}
      >
        <div
          style={{
            padding: "20px",
            borderBottom: "1px solid #1e293b",
            fontSize: "24px",
            fontWeight: "bold",
          }}
        >
          RepoMind AI Assistant
        </div>

        <div
          style={{
            flex: 1,
            overflowY: "auto",
            padding: "25px",
          }}
        >
          {messages.map((msg, index) => (
            <MessageBubble
              key={index}
              role={msg.role}
              message={msg.message}
            />
          ))}

          <div ref={messagesEndRef} />
        </div>

        <ChatInput onSend={handleSend} />
      </div>
    </div>
  );
}

export default ChatPage;