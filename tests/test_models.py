from src.models import UserCreate, UserLogin, TokenResponse


def test_user_create_model():
    user = UserCreate(email="test@example.com", password="pass123")
    assert user.email == "test@example.com"


def test_token_response_model():
    token = TokenResponse(access_token="abc123")
    assert token.token_type == "bearer"
