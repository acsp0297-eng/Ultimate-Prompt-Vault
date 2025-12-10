# UPHIGH ONLINE — Temporal‑Powered Automation Backend

Never Crash. Never Duplicate. Always Complete.

This package includes **Node.js (TypeScript-flavored JS)** and **Python** Temporal workers,
workflow blueprints (order fulfillment, affiliate payout, manual approval), an API/webhook template,
and a lightweight dashboard to approve/deny human‑in‑the‑loop steps. Use this as a starter kit and
customize the activities for your payment, CRM, and UID systems.

## Contents
- `backend_node/` — Node.js worker + workflows + activities (Temporal JS SDK)
- `backend_py/` — Python worker + workflows + activities (temporalio SDK)
- `api/` — Webhook handlers + n8n template
- `frontend/` — Minimal dashboard UI for workflow visibility + approvals
- `docs/` — Setup Guide (PDF & Markdown), API endpoints, diagrams
- `examples/` — Multilingual workflow snippets
- `temporal.yml` — Example local/Cloud namespace notes

## Quick Start (Node)
1. Install: `cd backend_node && npm i`
2. Copy env: `cp .env.example .env` and fill values.
3. Start Temporal: use Temporal Cloud (recommended) or `docker-compose` for local dev.
4. Run worker: `npm run worker`
5. Start API: `npm run api`
6. Open `/frontend/dashboard.html` in a static server to test approvals.

## Quick Start (Python)
1. Create venv and install: `cd backend_py && pip install -r requirements.txt`
2. `cp .env.example .env` and fill values.
3. Run worker: `python worker.py`

## Licensing
Starter license terms—adapt for your Beacons listing. Not legal advice.
