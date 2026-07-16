import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

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
          maxWidth: "75%",
          padding: "16px",
          borderRadius: "12px",
          background: isUser ? "#2563eb" : "#1f2937",
          color: "white",
        }}
      >
        {isUser ? (
          message
        ) : (
          <ReactMarkdown
            remarkPlugins={[remarkGfm]}
            components={{
              code({ inline, className, children, ...props }) {
                const match = /language-(\w+)/.exec(className || "");

                return !inline && match ? (
                  <SyntaxHighlighter
                    style={oneDark}
                    language={match[1]}
                    PreTag="div"
                    {...props}
                  >
                    {String(children).replace(/\n$/, "")}
                  </SyntaxHighlighter>
                ) : (
                  <code
                    style={{
                      background: "#111827",
                      padding: "2px 6px",
                      borderRadius: "4px",
                    }}
                    {...props}
                  >
                    {children}
                  </code>
                );
              },
            }}
          >
            {message}
          </ReactMarkdown>
        )}
      </div>
    </div>
  );
}

export default MessageBubble;