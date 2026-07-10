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
      <h1>RepoMind v2</h1>

      <p>AI Repository Assistant</p>

      <Link to="/chat">
        <button
          style={{
            marginTop: "20px",
            padding: "10px 20px",
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