from datetime import datetime


def format_timestamp(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def sanitize_email(email: str) -> str:
    return email.strip().lower()


def generate_user_id(email: str) -> str:
    import hashlib
    return hashlib.md5(email.encode()).hexdigest()[:12]
