# Cloud Infra Health Check Service

A minimal Flask API used as a deployment target for CI/CD pipeline demos (Azure DevOps).

## Endpoints

- `GET /health` — liveness check, returns `{"status": "ok"}`
- `GET /version` — returns the app version (from `APP_VERSION` env var)
- `GET /info` — returns hostname, version, and current UTC timestamp — useful for confirming which deployment/instance is responding

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Test

```bash
pytest
```

## Deploy

Deployed via an Azure DevOps YAML pipeline to Azure App Service (Free F1 tier).
