import axios from "axios";

const API = axios.create({
  baseURL: process.env.REACT_APP_API_URL || "http://localhost:4000/api"
});

export const getTodos = () => API.get("/todos");
export const addTodo = (title) => API.post("/todos", { title });
export const toggleTodo = (id) => API.put(`/todos/${id}`);
export const deleteTodo = (id) => API.delete(`/todos/${id}`);
