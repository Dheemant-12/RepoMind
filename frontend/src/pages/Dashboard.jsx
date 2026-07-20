import { useEffect, useState } from "react";
import {
  getDashboard,
  getRepositoryTree,
  getFileContent,
} from "../services/api";

function Dashboard() {
  const [data, setData] = useState(null);
  const [tree, setTree] = useState([]);
  const [selectedFile, setSelectedFile] = useState("");
  const [fileContent, setFileContent] = useState("Select a file to view its contents.");

  useEffect(() => {
    async function loadDashboard() {
      try {
        const dashboard = await getDashboard();
        setData(dashboard);

        const repository = await getRepositoryTree();
        setTree(repository.files);
      } catch (error) {
        console.error(error);
      }
    }

    loadDashboard();
  }, []);

  async function openFile(path) {
    try {
      setSelectedFile(path);

      const result = await getFileContent(path);

      setFileContent(result.content);
    } catch (error) {
      console.error(error);
      setFileContent("Unable to load file.");
    }
  }

  if (!data) {
    return (
      <div
        style={{
          background: "#0b1120",
          color: "white",
          minHeight: "100vh",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          fontSize: "24px",
        }}
      >
        Loading Dashboard...
      </div>
    );
  }

  const stats = [
    { title: "🐍 Python Files", value: data.python_files },
    { title: "⚙️ Functions", value: data.functions },
    { title: "🏛️ Classes", value: data.classes },
    { title: "📦 Imports", value: data.imports },
    {
      title: "📈 Avg Functions/File",
      value: data.avg_functions_per_file,
    },
  ];

  return (
    <div
      style={{
        background: "#0b1120",
        minHeight: "100vh",
        color: "white",
        padding: "30px",
      }}
    >
      <h1 style={{ marginBottom: "30px" }}>
        📊 RepoMind Dashboard
      </h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "320px 1fr",
          gap: "25px",
          alignItems: "start",
        }}
      >
        {/* Repository Explorer */}

        <div
          style={{
            background: "#1f2937",
            borderRadius: "12px",
            padding: "20px",
            maxHeight: "85vh",
            overflowY: "auto",
          }}
        >
          <h2>📁 Repository Explorer</h2>

          <p
            style={{
              color: "#9ca3af",
              marginBottom: "20px",
            }}
          >
            {data.repository}
          </p>

          {tree.length === 0 ? (
            <p>No files found.</p>
          ) : (
            tree.map((file, index) => (
              <div
                key={index}
                onClick={() => openFile(file)}
                style={{
                  padding: "8px",
                  marginBottom: "4px",
                  borderRadius: "6px",
                  cursor: "pointer",
                  background:
                    selectedFile === file
                      ? "#2563eb"
                      : "transparent",
                }}
              >
                📄 {file}
              </div>
            ))
          )}
        </div>

        {/* Right Side */}

        <div>
          {/* Repository Card */}

          <div
            style={{
              background: "#1f2937",
              padding: "20px",
              borderRadius: "12px",
            }}
          >
            <h2>{data.repository}</h2>

            <h3 style={{ marginTop: "15px" }}>
              ✅ Repository Status
            </h3>

            <p>Indexed Successfully</p>
          </div>

          {/* Metrics */}

          <div
            style={{
              display: "grid",
              gridTemplateColumns:
                "repeat(auto-fit, minmax(220px, 1fr))",
              gap: "20px",
              marginTop: "25px",
            }}
          >
            {stats.map((card) => (
              <div
                key={card.title}
                style={{
                  background: "#1f2937",
                  padding: "20px",
                  borderRadius: "12px",
                  textAlign: "center",
                }}
              >
                <h3>{card.title}</h3>

                <h1
                  style={{
                    marginTop: "10px",
                    fontSize: "40px",
                  }}
                >
                  {card.value}
                </h1>
              </div>
            ))}
          </div>

          {/* Repository Health */}

          <div
            style={{
              background: "#1f2937",
              padding: "25px",
              marginTop: "25px",
              borderRadius: "12px",
              textAlign: "center",
            }}
          >
            <h2>🏥 Repository Health</h2>

            <h1
              style={{
                fontSize: "60px",
                margin: "15px 0",
              }}
            >
              {data.health_score}/100
            </h1>

            <h2>{data.health_status}</h2>
          </div>

          {/* AI Summary */}

          <div
            style={{
              background: "#1f2937",
              padding: "25px",
              marginTop: "25px",
              borderRadius: "12px",
            }}
          >
            <h2>🤖 AI Summary</h2>

            <p
              style={{
                lineHeight: "1.8",
                marginTop: "15px",
              }}
            >
              {data.summary}
            </p>
          </div>

          {/* Code Viewer */}

          <div
            style={{
              background: "#111827",
              padding: "25px",
              marginTop: "25px",
              borderRadius: "12px",
            }}
          >
            <h2>📄 File Viewer</h2>

            <p
              style={{
                color: "#9ca3af",
                marginBottom: "15px",
              }}
            >
              {selectedFile || "No file selected"}
            </p>

            <pre
              style={{
                overflowX: "auto",
                whiteSpace: "pre-wrap",
                background: "#030712",
                padding: "20px",
                borderRadius: "8px",
                maxHeight: "600px",
                overflowY: "auto",
                fontSize: "14px",
              }}
            >
              <code>{fileContent}</code>
            </pre>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;