function MessageBubble({ role, message }) {
  const isUser = role === "user";

  return (
    <div
      style={{
        display: "flex",
        justifyContent: isUser ? "flex-end" : "flex-start",
        marginBottom: "20px",
      }}
    >
      <div
        style={{
          background: isUser ? "#2563eb" : "#1f2937",
          color: "white",
          padding: "15px",
          borderRadius: "12px",
          maxWidth: "70%",
          whiteSpace: "pre-wrap",
        }}
      >
        {message}
      </div>
    </div>
  );
}

export default MessageBubble;