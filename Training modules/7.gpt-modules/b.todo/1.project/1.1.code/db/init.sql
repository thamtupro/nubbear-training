CREATE DATABASE todo_app;
\c todo_app;

CREATE TABLE IF NOT EXISTS todos (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO todos(title) VALUES ('Learn K8s'), ('Add tracing');
