import { useState } from "react";

function ChatInput({ onSend }) {
  const [message, setMessage] = useState("");

  const handleSend = () => {
    if (!message.trim()) return;

    onSend(message);
    setMessage("");
  };

  return (
    <div
      style={{
        display: "flex",
        gap: "10px",
        padding: "20px",
        borderTop: "1px solid #333",
      }}
    >
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask anything about the repository..."
        style={{
          flex: 1,
          padding: "14px",
          borderRadius: "8px",
        }}
      />

      <button onClick={handleSend}>
        Send
      </button>
    </div>
  );
}

export default ChatInput;