import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export const analyzeRepository = async (repoUrl) => {
  const response = await api.post("/analyze", {
    repo_url: repoUrl,
  });

  return response.data;
};

export default api;