import { useEffect, useState } from "react";
import {
  getDashboard,
  getRepositoryTree,
  getDependencyGraph,
  getFileContent,
  explainFile,
  reviewFile,
} from "../services/api";

function Dashboard() {
  const [data, setData] = useState(null);
  const [tree, setTree] = useState([]);
  const [graph, setGraph] = useState({
    nodes: [],
    edges: [],
  });

  const [selectedFile, setSelectedFile] = useState("");
  const [fileContent, setFileContent] = useState(
    "Select a file to view its contents."
  );

  const [explanation, setExplanation] = useState("");
  const [review, setReview] = useState("");

  const [loadingExplanation, setLoadingExplanation] = useState(false);
  const [loadingReview, setLoadingReview] = useState(false);

  useEffect(() => {
    async function loadDashboard() {
      try {
        const dashboard = await getDashboard();
        setData(dashboard);

        const repository = await getRepositoryTree();
        setTree(repository.files);

        const dependencyGraph = await getDependencyGraph();
        setGraph(dependencyGraph);
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

      setExplanation("");
      setReview("");
    } catch (error) {
      console.error(error);
      setFileContent("Unable to load file.");
    }
  }

  async function handleExplainFile() {
    if (!selectedFile) return;

    try {
      setLoadingExplanation(true);

      const result = await explainFile(selectedFile);

      setExplanation(result.explanation);
    } catch (error) {
      console.error(error);
      setExplanation("Unable to generate explanation.");
    } finally {
      setLoadingExplanation(false);
    }
  }

  async function handleReviewFile() {
    if (!selectedFile) return;

    try {
      setLoadingReview(true);

      const result = await reviewFile(selectedFile);

      setReview(result.review);
    } catch (error) {
      console.error(error);
      setReview("Unable to generate review.");
    } finally {
      setLoadingReview(false);
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

  const graphStats = [
    {
      title: "📄 Files",
      value: graph.nodes.length,
    },
    {
      title: "🔗 Dependencies",
      value: graph.edges.length,
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

          {/* File Viewer */}

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

            <div
              style={{
                display: "flex",
                gap: "10px",
                marginBottom: "20px",
              }}
            >
              <button
                onClick={handleExplainFile}
                disabled={!selectedFile || loadingExplanation}
                style={{
                  padding: "10px 18px",
                  background: "#2563eb",
                  color: "white",
                  border: "none",
                  borderRadius: "6px",
                  cursor: "pointer",
                }}
              >
                {loadingExplanation
                  ? "Generating..."
                  : "🤖 Explain This File"}
              </button>

              <button
                onClick={handleReviewFile}
                disabled={!selectedFile || loadingReview}
                style={{
                  padding: "10px 18px",
                  background: "#16a34a",
                  color: "white",
                  border: "none",
                  borderRadius: "6px",
                  cursor: "pointer",
                }}
              >
                {loadingReview
                  ? "Reviewing..."
                  : "🔍 Review This File"}
              </button>
            </div>

            <pre
              style={{
                overflowX: "auto",
                whiteSpace: "pre-wrap",
                background: "#030712",
                padding: "20px",
                borderRadius: "8px",
                maxHeight: "500px",
                overflowY: "auto",
                fontSize: "14px",
              }}
            >
              <code>{fileContent}</code>
            </pre>
          </div>

          {/* AI Explanation */}

          <div
            style={{
              background: "#1f2937",
              padding: "25px",
              marginTop: "25px",
              borderRadius: "12px",
            }}
          >
            <h2>🧠 AI File Explanation</h2>

            <p
              style={{
                whiteSpace: "pre-wrap",
                lineHeight: "1.8",
                marginTop: "15px",
              }}
            >
              {explanation ||
                "Select a file and click 'Explain This File'."}
            </p>
          </div>

          {/* AI Code Review */}

          <div
            style={{
              background: "#1f2937",
              padding: "25px",
              marginTop: "25px",
              borderRadius: "12px",
            }}
          >
            <h2>🔍 AI Code Review</h2>

            <p
              style={{
                whiteSpace: "pre-wrap",
                lineHeight: "1.8",
                marginTop: "15px",
              }}
            >
              {review ||
                "Select a file and click 'Review This File'."}
            </p>
          </div>

          {/* Repository Dependency Graph */}

          <div
            style={{
              background: "#1f2937",
              padding: "25px",
              marginTop: "25px",
              borderRadius: "12px",
            }}
          >
            <h2>🌐 Repository Dependency Graph</h2>

            <div
              style={{
                display: "grid",
                gridTemplateColumns:
                  "repeat(auto-fit, minmax(220px, 1fr))",
                gap: "20px",
                marginTop: "20px",
              }}
            >
              {graphStats.map((card) => (
                <div
                  key={card.title}
                  style={{
                    background: "#111827",
                    padding: "20px",
                    borderRadius: "10px",
                    textAlign: "center",
                  }}
                >
                  <h3>{card.title}</h3>

                  <h1
                    style={{
                      fontSize: "42px",
                      marginTop: "10px",
                    }}
                  >
                    {card.value}
                  </h1>
                </div>
              ))}
            </div>

            <div
              style={{
                background: "#111827",
                marginTop: "25px",
                padding: "20px",
                borderRadius: "10px",
                maxHeight: "350px",
                overflowY: "auto",
              }}
            >
              <h3 style={{ marginBottom: "15px" }}>
                📌 Import Relationships
              </h3>

              {graph.edges.length === 0 ? (
                <p>No dependencies found.</p>
              ) : (
                graph.edges.map((edge, index) => (
                  <div
                    key={index}
                    style={{
                      padding: "12px",
                      marginBottom: "10px",
                      background: "#1f2937",
                      borderRadius: "8px",
                      borderLeft: "4px solid #2563eb",
                    }}
                  >
                    <div>
                      <strong>📄 From:</strong> {edge.from_node}
                    </div>

                    <div
                      style={{
                        margin: "8px 0",
                        color: "#60a5fa",
                      }}
                    >
                      ⬇ imports
                    </div>

                    <div>
                      <strong>📦 To:</strong> {edge.to_node}
                    </div>
                  </div>
                ))
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;