"""Auth service configuration settings."""
import os

SECRET_KEY = os.getenv("SECRET_KEY", "vertex-auth-service-secret-key-2024")
TOKEN_EXPIRE_MINUTES = int(os.getenv("TOKEN_EXPIRE_MINUTES", "60"))
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
