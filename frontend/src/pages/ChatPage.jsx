import { useState } from "react";
import ChatInput from "../components/ChatInput";
import MessageBubble from "../components/MessageBubble";
import { askRepository } from "../services/api";

function ChatPage() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      message:
        "👋 Hello! Your repository has been analyzed successfully.\n\nAsk me anything about the codebase.",
    },
  ]);

  const handleSend = async (message) => {
    // Show user message immediately
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        message,
      },
      {
        role: "assistant",
        message: "Thinking...",
      },
    ]);

    try {
      const response = await askRepository(message);

      setMessages((prev) => {
        const updated = [...prev];

        // Replace "Thinking..." with the AI answer
        updated[updated.length - 1] = {
          role: "assistant",
          message: response.answer,
        };

        return updated;
      });
    } catch (error) {
      console.error(error);

      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          role: "assistant",
          message:
            "❌ Failed to get a response from RepoMind. Please make sure the backend is running.",
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

        <p>📁 Current Repository</p>
      </div>

      {/* Chat Area */}
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

        {/* Input */}
        <ChatInput onSend={handleSend} />
      </div>
    </div>
  );
}

export default ChatPage;