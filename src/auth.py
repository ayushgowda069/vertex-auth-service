"""JWT authentication logic — CRITICAL FILE."""
import jwt
import hashlib
from datetime import datetime, timedelta
from typing import Optional

SECRET_KEY = "vertex-auth-service-secret-key-2024"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 60


def create_token(data: dict) -> str:
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(plain: str, hashed: str) -> bool:
    return hash_password(plain) == hashed

# vertexci-sim:396e3bc9 t=1778739803
# change line 0: 4907d42fdea847de
# change line 1: 2ed842a5e67a44f6
# change line 2: e6f1dab07b7b4afa
# change line 3: 1bf53df0241940cb
# change line 4: d6a11c6b8564401d
# change line 5: f245cb0e1f5d4ea1
# change line 6: fc8070466140474b
# change line 7: d25fcfad47354bcd
# change line 8: 46465375eee64e1f
# change line 9: 1cf90248750d4152
# change line 10: aac910fc2a244992
# change line 11: 2dea20e37cbf4133
# change line 12: be15bde05eea4b13
# change line 13: cf34ec77bfa940e5
# change line 14: 0a53f72b5a3e4ad1
# change line 15: fed0ababadea43a5
# change line 16: fb08097de15e443e
# change line 17: ecc8a1fdb81e4f8e
# change line 18: 958a43f6732e4e10
# change line 19: 6247780dddb64280
# change line 20: 5aa1f5e7add3445d
# change line 21: 887c1b7f46a74d29
# change line 22: d46176edebf44d79
# change line 23: 37e6baa52f3546da
# change line 24: b43427f340e64180
# change line 25: 7db2e7a0805f4904
# change line 26: 548cf703d93d4258
# change line 27: 9b2734923c7d498e
# change line 28: d6aad562789d4dbd
# change line 29: 81a0b19c0d05430d
# change line 30: 148c20cad14a4119
# change line 31: 086146180223428b
# change line 32: 0b56dfeff269422b
# change line 33: 092727cd0bdc4ea8
# change line 34: 45b6b68f0f6a4a7f
# change line 35: 94d0f8b22ec9417e
# change line 36: df1b8542a9634a58
# change line 37: dd53c04e4cfa40c1
# change line 38: 7bddead54eed4773
# change line 39: 4d62b32a3b894b5a
# change line 40: 60c8701815064c01
# change line 41: a4658e58898049f4
# change line 42: 136a79540dd44ae0
# change line 43: 61afe8781b2b4b1a
# change line 44: 3c6384e208684ed0
# change line 45: 207f577fd4de45fa
# change line 46: ac0fd1a0faee468e
# change line 47: 80bc79fba987491b
# change line 48: 90c6b659d8b54cec
# change line 49: b217d0a0ca054976
# change line 50: b238f04202df4579
# change line 51: 768e52371f2c4e16
# change line 52: 581464cb66f24cfb
# change line 53: e5657a22bbe34790
# change line 54: e797402b0c2d4d0e
# change line 55: 2af6be68f5074b36
# change line 56: 291b9955a2f841ab
# change line 57: 49d647fe19614080
# change line 58: 194a60a298ba46dd
# change line 59: 4856e2f927d94d19
# change line 60: 068924d598d548a5
# change line 61: eb4f8c378ec74178
# change line 62: 98692352bd024f4f
# change line 63: 3d3d2eedc8e942a7
# change line 64: 06b8b816c8074a88
# change line 65: 95318d8cc8734729
# change line 66: 4dca79d7a2a84d71
# change line 67: f78b9d3dd1034e56
# change line 68: fe3d2cc35f864247
# change line 69: 055bd60af6714f7a
# change line 70: 6591806474864f21
# change line 71: 6340ee4469394b8d
