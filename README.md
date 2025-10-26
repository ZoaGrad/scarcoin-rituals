# ScarCoin Rituals

ScarCoin Rituals is the reference implementation for the ScarIndex oracle, a protocol component that computes a community-focused ScarIndex from multiple real-time feeds (narrative coherence, social resonance, economic stability, technical health) and provides attestation for on-chain anchoring.

This repository contains:

- A FastAPI-based ScarIndex Oracle (`oracle/scarindex_service.py`) that computes the ScarIndex, produces attestations, and exposes REST endpoints.
- An async CTMS connector (`integration/ctms_connector.py`) to fetch narrative coherence metrics.
- Configuration and environment management (`core/config.py` and `.env.example`).
- Tests under `tests/` including unit tests and API endpoint integration tests.
- A multi-stage `Dockerfile` for production image builds.
- A GitHub Actions CI workflow at `.github/workflows/ci.yml` for testing, linting, security scans, and container validation.

Quick links
- Source: ./oracle
- Integration connectors: ./integration
- Tests: ./tests
- CI workflow: ./.github/workflows/ci.yml

## Getting started (local development)

Prerequisites:

- Python 3.11+ (project created with 3.12 in dev container)
- Docker (for container runs)

Steps:

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create `.env` from the example and update values:

```bash
cp .env.example .env
# Edit .env with real values
```

4. Run the test suite (fast):

```bash
./.venv/bin/python -m pytest tests/ -v
```

5. Start the ScarIndex Oracle (development):

```bash
./.venv/bin/uvicorn oracle.scarindex_service:app --host 0.0.0.0 --port 8000 --reload
```

6. Endpoints:

- Health: GET /health
- Compute ScarIndex: POST /compute-scarindex
- F4 trigger check: GET /f4-trigger-check

## Docker (production image)

Build and run the container:

```bash
docker build -t scarcoin-oracle:latest .
docker run -d -p 8000:8000 --env-file .env --name scarcoin-oracle scarcoin-oracle:latest
```

Health check is exposed at `/health` (Dockerfile includes a HEALTHCHECK instruction).

## CI / CD

This repository includes a GitHub Actions workflow that:

- Runs tests across multiple Python versions
- Runs linting (Black, flake8, isort)
- Performs security scans with Bandit (and Trivy in the docker job)
- Builds and validates the Docker image
- Optionally uploads coverage reports to Codecov (configure token in repository secrets)

Add required secrets in your repository settings for full CI features (CODECOV token, Docker registry creds if pushing images, etc.).

## Development notes

- Replace the mock connectors in `oracle/scarindex_service.py` with production-ready connectors as they become available.
- The CTMS connector is implemented in `integration/ctms_connector.py` and is used by the ScarIndex service.
- Attestation/signing is currently a placeholder (`generate_attestation`) and should be replaced with a secure signing implementation using the project's key management approach.

## Running the provided setup script

There is a helper script `setup_ci_environment.sh` that will create test directories and install dev dependencies. Use it in a dev environment (it runs pip install -r requirements.txt and pytest).

```bash
chmod +x setup_ci_environment.sh
./setup_ci_environment.sh
```

## Testing and coverage

- Run full tests with coverage and HTML report:

```bash
./.venv/bin/python -m pytest tests/ -v --cov=./ --cov-report=html
# Open htmlcov/index.html
```

## Contributing

Please open issues and pull requests. Use the supplied PR template (`.github/pull_request_template.md`). Follow code style guidelines (Black) and add tests for new features.

## License

Add your license here (MIT, Apache-2.0, etc.) or include a LICENSE file.

---

If you'd like, I can also add a short `CONTRIBUTING.md`, CODEOWNERS, or a license file — tell me which one and I'll create it.

