# DevOps Roadmap — Todo App+ Project

## Phase A — Core MVP
1. Backend (Node.js/Express + PostgreSQL)
   - CRUD Todo
   - /health, /metrics (Prometheus)
   - OpenTelemetry tracing (Jaeger)
   - Logging JSON (pino) + trace_id
2. Frontend (Nginx serve static)
   - Call API /api/*
   - (chuẩn bị để thêm auth sau này)
3. Kubernetes cơ bản
   - Deployment + Service cho BE/FE
   - StatefulSet + PVC cho PostgreSQL
   - Ingress route FE + BE (chưa TLS)

---

## Phase B — Observability-first
4. Metrics
   - Prometheus Operator (ServiceMonitor)
   - Grafana dashboard cho app + infra
5. Tracing
   - OpenTelemetry Collector
   - Jaeger/Tempo, propagate trace-id từ FE → BE
6. Logging
   - Pino → Filebeat/Fluentbit → Logstash
   - Elasticsearch + Kibana
   - Logs gắn trace_id

---

## Phase C — Auth & Secrets
7. Keycloak (OIDC)
   - FE: login qua Keycloak adapter JS
   - BE: verify JWT qua JWKS
   - Bảo vệ `/api/*`
8. Vault (Secret Management)
   - KV Engine cho DB creds, JWT secret
   - Kubernetes Auth + ServiceAccount
   - (nâng cao) Database Secrets Engine → cấp dynamic credentials cho Postgres

---

## Phase D — Performance & Scale
9. Redis cache
   - Cache list todos, detail
   - HPA cho BE
   - Requests/limits CPU & RAM
   - PgBouncer (connection pool)
   - (optional) Postgres read-replica
