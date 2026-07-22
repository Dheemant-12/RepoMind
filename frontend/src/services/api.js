import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
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

export const askRepository = async (question) => {
  const response = await api.post("/ask", {
    question,
  });

  return response.data;
};

export const getDashboard = async () => {
  const response = await api.get("/dashboard");
  return response.data;
};

export const getRepositoryTree = async () => {
  const response = await api.get("/repository-tree");
  return response.data;
};

export const getFileContent = async (path) => {
  const response = await api.get("/file-content", {
    params: {
      path,
    },
  });

  return response.data;
};

export const explainFile = async (filePath) => {
  const response = await api.post("/explain-file", {
    file_path: filePath,
  });

  return response.data;
};

export const reviewFile = async (filePath) => {
  const response = await api.post("/review-file", {
    file_path: filePath,
  });

  return response.data;
};

export default api;