import pytest
from src.auth import create_token, verify_token, hash_password, verify_password


def test_create_and_verify_token():
    token = create_token({"sub": "test@example.com", "role": "user"})
    payload = verify_token(token)
    assert payload is not None
    assert payload["sub"] == "test@example.com"


def test_invalid_token():
    result = verify_token("not.a.real.token")
    assert result is None


def test_password_hashing():
    hashed = hash_password("secret123")
    assert verify_password("secret123", hashed)
    assert not verify_password("wrong", hashed)
