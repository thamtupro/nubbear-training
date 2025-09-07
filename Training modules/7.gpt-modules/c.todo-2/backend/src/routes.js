const express = require("express");
const router = express.Router();
const { Todo } = require("./models");

// Get all todos
router.get("/todos", async (req, res) => {
  const todos = await Todo.findAll();
  res.json(todos);
});

// Create new todo
router.post("/todos", async (req, res) => {
  const todo = await Todo.create({ title: req.body.title });
  res.json(todo);
});

// Toggle complete
router.put("/todos/:id", async (req, res) => {
  const todo = await Todo.findByPk(req.params.id);
  if (!todo) return res.status(404).json({ error: "Not found" });
  todo.completed = !todo.completed;
  await todo.save();
  res.json(todo);
});

// Delete
router.delete("/todos/:id", async (req, res) => {
  const todo = await Todo.findByPk(req.params.id);
  if (!todo) return res.status(404).json({ error: "Not found" });
  await todo.destroy();
  res.json({ message: "Deleted" });
});

module.exports = router;
