# Cloud Infra Health Check Service

A minimal Flask API used as a deployment target for CI/CD pipeline demos (Azure DevOps).

**Live demo**: https://cloud-infra-health-check-bimscreator-dcc0egfacceyhnac.ukwest-01.azurewebsites.net/health

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

## CI/CD

Deployed via an Azure DevOps YAML pipeline ([azure-pipelines.yml](azure-pipelines.yml)) to Azure App Service (Free F1 tier). On every push to `main`:

1. **Build stage** — installs dependencies, runs `pytest`
2. **Deploy stage** — packages the app and deploys it to Azure App Service (Linux, Python 3.11)
