import { useEffect, useState } from "react";
import { getDashboard } from "../services/api";

function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    async function loadDashboard() {
      try {
        const result = await getDashboard();
        setData(result);
      } catch (error) {
        console.error("Failed to load dashboard:", error);
      }
    }

    loadDashboard();
  }, []);

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
        Loading dashboard...
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
        padding: "40px",
      }}
    >
      <h1 style={{ marginBottom: "20px" }}>
        📊 RepoMind Dashboard
      </h1>

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
          gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
          gap: "20px",
          marginTop: "30px",
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
                fontSize: "42px",
              }}
            >
              {card.value}
            </h1>
          </div>
        ))}
      </div>

      {/* Health Card */}
      <div
        style={{
          background: "#1f2937",
          marginTop: "30px",
          padding: "25px",
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
          marginTop: "30px",
          padding: "25px",
          borderRadius: "12px",
        }}
      >
        <h2>🤖 AI Summary</h2>

        <p
          style={{
            marginTop: "15px",
            lineHeight: "1.8",
            fontSize: "17px",
          }}
        >
          {data.summary}
        </p>
      </div>
    </div>
  );
}

export default Dashboard;