# vertex-auth-service

JWT-based authentication microservice for the VertexCI platform.

## Endpoints
- `POST /auth/register` — Register a new user
- `POST /auth/login` — Get JWT token  
- `GET /auth/me` — Get current user info (requires token)
- `GET /health` — Health check

## Run locally
```bash
pip install -r requirements.txt
python main.py
```

## Run tests
```bash
pytest tests/
```
