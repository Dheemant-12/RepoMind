function Dashboard() {
  const stats = [
    { title: "Python Files", value: 42 },
    { title: "Functions", value: 318 },
    { title: "Classes", value: 61 },
    { title: "Imports", value: 425 },
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
        <h2>Repository</h2>
        <p>Flask</p>

        <h3 style={{ marginTop: "20px" }}>
          ✅ Repository Status
        </h3>

        <p>Indexed Successfully</p>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(2,1fr)",
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

        <p>
          Flask is a lightweight Python web framework.
          The repository contains modular routing,
          request handling, template rendering,
          and extension support.
        </p>
      </div>
    </div>
  );
}

export default Dashboard;