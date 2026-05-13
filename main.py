from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.auth import create_token, verify_token
from src.models import UserCreate, UserLogin, TokenResponse

app = FastAPI(title="Vertex Auth Service", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# In-memory user store (demo only)
USERS_DB: dict = {}


@app.post("/auth/register")
async def register(user: UserCreate):
    if user.email in USERS_DB:
        raise HTTPException(status_code=400, detail="Email already registered")
    USERS_DB[user.email] = {"email": user.email, "password": user.password, "role": "user"}
    return {"message": "User registered successfully"}


@app.post("/auth/login", response_model=TokenResponse)
async def login(form: UserLogin):
    user = USERS_DB.get(form.email)
    if not user or user["password"] != form.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token({"sub": form.email, "role": user["role"]})
    return TokenResponse(access_token=token, token_type="bearer")


@app.get("/auth/me")
async def get_me(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"email": payload.get("sub"), "role": payload.get("role")}


@app.get("/health")
async def health():
    return {"status": "ok", "service": "vertex-auth-service"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
