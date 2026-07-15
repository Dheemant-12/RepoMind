import { useState } from "react";

function ChatInput({ onSend }) {
  const [message, setMessage] = useState("");

  const handleSend = () => {
    if (!message.trim()) return;

    onSend(message);
    setMessage("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div
      style={{
        display: "flex",
        gap: "10px",
        padding: "20px",
        borderTop: "1px solid #333",
        background: "#111827",
      }}
    >
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Ask anything about the repository..."
        style={{
          flex: 1,
          padding: "14px",
          borderRadius: "8px",
          border: "none",
          outline: "none",
          fontSize: "16px",
        }}
      />

      <button
        onClick={handleSend}
        style={{
          padding: "14px 24px",
          cursor: "pointer",
        }}
      >
        Send
      </button>
    </div>
  );
}

export default ChatInput;