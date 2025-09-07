import express from 'express';
import pkg from 'pg';
import pino from 'pino';
import client from 'prom-client';
import { context, trace } from '@opentelemetry/api';

const { Pool } = pkg;
const app = express();
app.use(express.json());

const logger = pino();
const port = process.env.PORT || 3000;

// Prometheus metrics
const register = new client.Registry();
client.collectDefaultMetrics({ register });
const httpRequestCounter = new client.Counter({
  name: 'http_requests_total',
  help: 'Total HTTP requests',
  labelNames: ['route', 'method', 'status']
});
register.registerMetric(httpRequestCounter);

// DB config
const pool = new Pool({
  host: process.env.DB_HOST || 'localhost',
  port: +(process.env.DB_PORT || 5432),
  user: process.env.DB_USER || 'postgres',
  password: process.env.DB_PASS || 'postgres',
  database: process.env.DB_NAME || 'todo_app'
});

// middleware: gắn trace_id vào log
app.use((req, res, next) => {
  const span = trace.getSpan(context.active());
  const traceId = span?.spanContext()?.traceId;
  req.log = logger.child({ trace_id: traceId });
  const start = Date.now();

  res.on('finish', () => {
    httpRequestCounter.labels(req.path, req.method, String(res.statusCode)).inc();
    req.log.info({ method: req.method, path: req.path, status: res.statusCode, latency_ms: Date.now() - start }, 'http_access');
  });

  next();
});

// health & metrics
app.get('/health', (_req, res) => res.send('OK'));
app.get('/metrics', async (_req, res) => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});

// CRUD
app.get('/api/todos', async (_req, res) => {
  const { rows } = await pool.query('SELECT id, title, created_at FROM todos ORDER BY id DESC');
  res.json(rows);
});

app.post('/api/todos', async (req, res) => {
  const { title } = req.body || {};
  await pool.query('INSERT INTO todos(title) VALUES($1)', [title]);
  res.status(201).json({ message: 'created' });
});

app.delete('/api/todos/:id', async (req, res) => {
  await pool.query('DELETE FROM todos WHERE id=$1', [req.params.id]);
  res.json({ message: 'deleted' });
});

app.listen(port, () => logger.info(`Backend running on :${port}`));
