import React, { useEffect, useState } from "react";
import { getTodos, addTodo, toggleTodo, deleteTodo } from "./api";

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState("");

  useEffect(() => {
    loadTodos();
  }, []);

  const loadTodos = async () => {
    const res = await getTodos();
    setTodos(res.data);
  };

  const handleAdd = async () => {
    if (!newTodo.trim()) return;
    await addTodo(newTodo);
    setNewTodo("");
    loadTodos();
  };

  const handleToggle = async (id) => {
    await toggleTodo(id);
    loadTodos();
  };

  const handleDelete = async (id) => {
    await deleteTodo(id);
    loadTodos();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Todo App</h1>
      <input
        value={newTodo}
        onChange={(e) => setNewTodo(e.target.value)}
        placeholder="New task..."
      />
      <button onClick={handleAdd}>Add</button>
      <ul>
        {todos.map((t) => (
          <li key={t.id}>
            <span
              onClick={() => handleToggle(t.id)}
              style={{
                textDecoration: t.completed ? "line-through" : "none",
                cursor: "pointer"
              }}
            >
              {t.title}
            </span>
            <button onClick={() => handleDelete(t.id)} style={{ marginLeft: "10px" }}>
              ❌
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
