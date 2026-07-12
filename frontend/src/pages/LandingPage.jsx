import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { analyzeRepository } from "../services/api";

function LandingPage() {
  const [repoUrl, setRepoUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  const handleAnalyze = async () => {
    if (!repoUrl.trim()) {
      alert("Enter a GitHub Repository URL");
      return;
    }

    try {
      setLoading(true);

      await analyzeRepository(repoUrl);

      alert("Repository analyzed successfully!");

      navigate("/chat");
    } catch (err) {
      console.error(err);
      alert("Analysis failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        background: "#111827",
        color: "white",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <h1 style={{ fontSize: "48px" }}>RepoMind</h1>

      <p>AI Repository Assistant</p>

      <input
        value={repoUrl}
        onChange={(e) => setRepoUrl(e.target.value)}
        placeholder="https://github.com/user/repository"
        style={{
          width: "500px",
          padding: "15px",
          marginTop: "30px",
          borderRadius: "8px",
          border: "none",
        }}
      />

      <button
        onClick={handleAnalyze}
        style={{
          marginTop: "20px",
          padding: "15px 40px",
          fontSize: "18px",
          cursor: "pointer",
        }}
      >
        {loading ? "Analyzing..." : "Analyze Repository"}
      </button>
    </div>
  );
}

export default LandingPage;