import { useState } from "react";
import ChatInput from "../components/ChatInput";
import MessageBubble from "../components/MessageBubble";

function ChatPage() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      message:
        "👋 Hello! Your repository has been analyzed successfully.\n\nAsk me anything about the codebase.",
    },
  ]);

  const handleSend = (message) => {
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        message,
      },
      {
        role: "assistant",
        message:
          "This is a placeholder response.\nTomorrow we'll connect this to the RepoMind AI backend.",
      },
    ]);
  };

  return (
    <div
      style={{
        display: "flex",
        height: "100vh",
        background: "#0f172a",
        color: "white",
      }}
    >
      {/* Sidebar */}
      <div
        style={{
          width: "260px",
          borderRight: "1px solid #1e293b",
          padding: "20px",
          background: "#111827",
        }}
      >
        <h2>RepoMind</h2>

        <button
          style={{
            width: "100%",
            marginTop: "20px",
            padding: "12px",
            cursor: "pointer",
          }}
        >
          + New Chat
        </button>

        <hr style={{ margin: "20px 0" }} />

        <h3>Repositories</h3>

        <p>📁 Flask</p>
      </div>

      {/* Chat Section */}
      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
        }}
      >
        {/* Header */}
        <div
          style={{
            padding: "20px",
            borderBottom: "1px solid #1e293b",
            fontSize: "24px",
            fontWeight: "bold",
          }}
        >
          RepoMind AI
        </div>

        {/* Messages */}
        <div
          style={{
            flex: 1,
            overflowY: "auto",
            padding: "20px",
          }}
        >
          {messages.map((msg, index) => (
            <MessageBubble
              key={index}
              role={msg.role}
              message={msg.message}
            />
          ))}
        </div>

        {/* Chat Input */}
        <ChatInput onSend={handleSend} />
      </div>
    </div>
  );
}

export default ChatPage;