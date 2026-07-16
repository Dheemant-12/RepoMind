import { useEffect, useRef, useState } from "react";
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
    const chatName = `Chat ${chatHistory.length + 1}`;

    setChatHistory((prev) => [...prev, chatName]);

    setMessages([
      {
        role: "assistant",
        message:
          "👋 New chat started.\n\nAsk me anything about the repository.",
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
    } catch (err) {
      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          role: "assistant",
          message:
            "❌ Unable to contact the backend. Please make sure FastAPI is running.",
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
          background: "#111827",
          borderRight: "1px solid #1e293b",
          padding: "20px",
        }}
      >
        <h2>RepoMind</h2>

        <button
          onClick={handleNewChat}
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

        <h3>Chat History</h3>

        {chatHistory.map((chat, index) => (
          <p key={index}>💬 {chat}</p>
        ))}

        <hr style={{ margin: "20px 0" }} />

        <h3>Repository</h3>

        <p>📁 Flask</p>
      </div>

      {/* Chat Area */}
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
            fontWeight: "bold",
            fontSize: "24px",
          }}
        >
          RepoMind AI
        </div>

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

          <div ref={messagesEndRef} />
        </div>

        <ChatInput onSend={handleSend} />
      </div>
    </div>
  );
}

export default ChatPage;