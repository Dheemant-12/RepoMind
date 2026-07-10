import { Link } from "react-router-dom";

function LandingPage() {
  return (
    <div
      style={{
        height: "100vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        background: "#0f172a",
        color: "white",
      }}
    >
      <h1 style={{ fontSize: "3rem" }}>RepoMind v2</h1>

      <p style={{ marginTop: "10px", color: "#cbd5e1" }}>
        AI-Powered Repository Assistant
      </p>

      <Link to="/chat">
        <button
          style={{
            marginTop: "30px",
            padding: "12px 25px",
            fontSize: "16px",
            cursor: "pointer",
          }}
        >
          Launch RepoMind
        </button>
      </Link>
    </div>
  );
}

export default LandingPage;