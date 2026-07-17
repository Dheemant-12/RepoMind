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
    { title: "Python Files", value: data.python_files },
    { title: "Functions", value: data.functions },
    { title: "Classes", value: data.classes },
    { title: "Imports", value: data.imports },
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
      <h1>📊 RepoMind Dashboard</h1>

      <div
        style={{
          background: "#1f2937",
          padding: "20px",
          borderRadius: "10px",
          marginTop: "25px",
        }}
      >
        <h2>{data.repository}</h2>

        <h3 style={{ marginTop: "20px" }}>
          ✅ Repository Status
        </h3>

        <p>Indexed Successfully</p>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(2, 1fr)",
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
              borderRadius: "10px",
            }}
          >
            <h3>{card.title}</h3>
            <h1>{card.value}</h1>
          </div>
        ))}
      </div>

      <div
        style={{
          background: "#1f2937",
          marginTop: "30px",
          padding: "20px",
          borderRadius: "10px",
        }}
      >
        <h2>AI Summary</h2>

        <p>{data.summary}</p>
      </div>
    </div>
  );
}

export default Dashboard;