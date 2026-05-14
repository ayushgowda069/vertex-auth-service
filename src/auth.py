"""JWT authentication logic — CRITICAL FILE."""
# pyrefly: ignore [missing-import]
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

# vertexci-sim:59b5cea3 t=1778700156
# change line 0: 02232f5813d7403d
# change line 1: f96c6d1a545e4829
# change line 2: b2628ce5b5ae4ede
# change line 3: d99a65d9f1bd43e6
# change line 4: 33b3e80ce9c04e97
# change line 5: dcf0e13bb3d04d78
# change line 6: 9155e3d28f4d465c
# change line 7: 2869a280de2e4643
# change line 8: 3f5b3d34f0dd4e7a
# change line 9: bf0d53beb06e4f33
# change line 10: 1a44b156ab1946bb
# change line 11: 327cec65e46c4bb7
# change line 12: 7771ffae2f914b69
# change line 13: 9a4274162aab4761
# change line 14: a2a8beeb71284979
# change line 15: 23fd2fab92c94f8a
# change line 16: c0439006b9824530
# change line 17: 2906dc97e9bb4c9a
# change line 18: f84bd6e4d5df4d7a
# change line 19: e878f2e43bb14f83
# change line 20: cac98237375a411a
# change line 21: e9623cb9d32a41f8
# change line 22: 59d1c27a3d8748ac
# change line 23: a10a63cc048d4943
# change line 24: 2aaf1e3f308443ee
# change line 25: 920659398d2742e2
# change line 26: ea4c4da2b51542b3
# change line 27: 44b98615888d4820
# change line 28: b1a3be775f184a3b
# change line 29: b40bbe1c3f904223
# change line 30: 22cf75f4758445a2
# change line 31: 5d21a7a784644fc6
# change line 32: d8e8840261c24f8a
# change line 33: 8f931cb6b6014427
# change line 34: fc715b162f884e0f
# change line 35: fbacb8d7f6c74882
# change line 36: d0083c76220f4a6c
# change line 37: 0dba819a6eb840dc
# change line 38: b066a1f3ca794700
# change line 39: d1380c6a9b1c4294
# change line 40: 902a74a5d322453e
# change line 41: 270646ea77de4aba
# change line 42: f7ef5f800c6d4018
# change line 43: 1e78ed3b22294ce1
# change line 44: cc3ec44d58304fa7
# change line 45: 38007274a5074264
# change line 46: bd56ac86cf36474e
# change line 47: 7337d800b928428d
# change line 48: 1067531730634f0a
# change line 49: 7466a933a4e34578
# change line 50: b04975210df54e5f
# change line 51: ffe4bf6cfa9244a5
# change line 52: 521e1496086d40a1
# change line 53: c47a5c09f5204d02
# change line 54: 8b1e3f1e2a5246ef
# change line 55: 4a91680c3b1442c1
# change line 56: 9436f060a91b4413
# change line 57: c83e7ac528f64fd1
# change line 58: 271c37202ce746a4
# change line 59: c50c6ddb23d64000
# change line 60: 97807241384c407c
# change line 61: 74336dc6973a40d6
# change line 62: 58f803475a874a2c
# change line 63: 1cc56c01b0a9406e
# change line 64: 8dbb96413e80400c
# change line 65: 3bd3079684c34cfa
# change line 66: 3d0f51317d024a9b
# change line 67: dde618e3680a4181
# change line 68: 283c4cb5aba243c4
# change line 69: d2c7950aa9174dea
# change line 70: f1e9d113bd4c44ed
# change line 71: 88700a24125f405f
# change line 72: 6a195d001c444e3b
# change line 73: 9360c7815dcd4fd2
# change line 74: 6bab08aec1224d66
# change line 75: e563eb4538964d89
# change line 76: 9c62b92293044a96
# change line 77: 838b2f7215cd4099
# change line 78: 4d41adc8d07c4497
# change line 79: be90423eea2f4c56
# change line 80: 6e6fe627804a4773
# change line 81: a5fa21ea08254c48
# change line 82: a98c53858e6345ac
# change line 83: f5c3c287a9324e2a
# change line 84: 84c0bf74d948450a
# change line 85: 986ce871b9e146aa
# change line 86: c3511e8cc26a4a74
# change line 87: a1c2ce6d7d4e4e2d
# change line 88: 66f0e1282b154862
# change line 89: 9c6d92e27cc540f9
# change line 90: 63a04aebd6f048fe
# change line 91: 9916aea8597b4362
# change line 92: 5de9cfb3c3504b35
# change line 93: 502ec43ad9564601
# change line 94: 00ef8d1b0e094529
# change line 95: 9edfbf8269c4428a
# change line 96: 10e787e1919f4e1b
# change line 97: 34dc167c9a864de9
# change line 98: 485cc752d07041f4
# change line 99: 2cda82d94b624a1e
# change line 100: dd0589dbf4d44879
# change line 101: f914e8f7127543e7
# change line 102: 3344b12314bc47bd
# change line 103: 58c344760fbe41c9
# change line 104: eddc1c137f1a478b
# change line 105: d560e5c2c98445f0
# change line 106: 5d6215e820fc43ee
# change line 107: 9f93a323f2044d39
# change line 108: a6f1ba05c3474706
# change line 109: d08f15823d744317
# change line 110: a7ac357d1c144453
# change line 111: 5561bbc223dd4234
# change line 112: 6de8bfe236f04508
# change line 113: eb32738a6b1b4880
# change line 114: 1f06198530754bfd
# change line 115: d20891b1fd894184
# change line 116: 061f3b053f4f4e69
# change line 117: 46f2befab3064959
# change line 118: fe3fab8b53ba44a9
# change line 119: 6bd42ec2333045e8
# change line 120: 275a3cdc5b4c43ff
# change line 121: 996500c0d978460a
# change line 122: 2f13919136eb446e
# change line 123: 67c343e238d74ee5
# change line 124: 5bf370b7301041dc
# change line 125: 667b07f50f314931
# change line 126: 0606739a73b34ea8
# change line 127: ad19ed60a0104be1
# change line 128: 4df95f027a824496
# change line 129: 46937879949c4dde
# change line 130: d3ad02cf24a047de
# change line 131: f95ad8b9f9be42f4
# change line 132: 3c77d554bb814f22
# change line 133: 099c8ed1d77246b8
# change line 134: 42a1feee1e9a4dc9
# change line 135: 2920f69b08874d98
# change line 136: 0d6a064722ae4575
# change line 137: 9b71d97361634391
# change line 138: 29c7ea8314b54c70
# change line 139: 9fa23af6be994a88
# change line 140: c49176a89c96420d
# change line 141: 2a9825adbc064814
# change line 142: 8dda6b4584f84a1f
# change line 143: 353480c9c3f94e6a
# change line 144: 5566bae62487421a
# change line 145: 6edce51e5b204de0
# change line 146: 45de31a6326d4fa4
# change line 147: aabe037d115d48cf
# change line 148: 406e8a18c98b4a93
# change line 149: 8df074c80bc64138
# change line 150: 543ef220a7bd404f
# change line 151: b3ea6d551398429f
# change line 152: 13a066fd40b24517
# change line 153: dd4af665fe424594
# change line 154: 5c48fea3e006421b

# vertexci-sim:6918e7f2 t=1778700171
# change line 0: 578ec6e555164d1e
# change line 1: 4b65e9b419f04678
# change line 2: d9e1e57c6dcb441c
# change line 3: edf9b50f01834073
# change line 4: d9ce99fb6f624280
# change line 5: 0cf80691907b4814
# change line 6: 3346fdc433ee4964
# change line 7: 33db0463d6d84f82
# change line 8: 4c457cd7e25d4fc3
# change line 9: 0c937feb0f0947b8
# change line 10: 0c46bd2d187c4041
# change line 11: b630a41922a9448e
# change line 12: 8eb9421f65274076
# change line 13: 8bca9790e1564f62
# change line 14: 822d591351964b1e
# change line 15: a7c6a5dfb6b34419
# change line 16: 1ad1a9e4b63e4401
# change line 17: 9584642799dc4525
# change line 18: c0b81e2d05834b77
# change line 19: d11ab631dea04b91
# change line 20: 1ed30175fed74a80
# change line 21: ac094d7b80aa4509
# change line 22: e90a6a76e1344654
# change line 23: 107f86c7e67b444b
# change line 24: 835acc9246a74650
# change line 25: 7bc3fd18339f4296
# change line 26: fa50d5ccfa054d86
# change line 27: 71a8f0c38a844de9
# change line 28: 6c0df203d5cd4324
# change line 29: e0be4458e61c4473
# change line 30: 34e4ed3204604e08
# change line 31: 3e880a7a444f40a3
# change line 32: 256eca2c21274641
# change line 33: 92098110afc64a4b
# change line 34: 67000ebfbca344d1
# change line 35: 98aac71b8d6f4351
# change line 36: 75cfe78c31634f1c
# change line 37: 34189b39131b4caa
# change line 38: 01e3e69b421f45ed
# change line 39: 6fbcd4e851bb436f
# change line 40: 97523516fe2b4e7f
# change line 41: cd9c4eab69a24eb5
# change line 42: 020f9d03f34d4e03
# change line 43: c7a83233d94a472c
# change line 44: af74b3680d1c458b
# change line 45: 7578d4915d7643fd
# change line 46: 17265e5445c44683
# change line 47: 265ae222ee244170
# change line 48: af562f41b68e4bed
# change line 49: e34a1cdb604c4bde
# change line 50: c671df98bc974145
# change line 51: 62cbd8d70d0246e3
#my changes111 ff sssss
#xxxx111

# vertexci-sim:ff1a8328 t=1778749093
# change line 0: 01fd08ad3b5b4ff4
# change line 1: be927b84c71a48d0
# change line 2: c236bc9320dd4f89
# change line 3: 33341f90ebf44345
# change line 4: 9f7e67912e354d5f
# change line 5: bafe78b89aa04dad
# change line 6: 650b981184f9449a
# change line 7: 677f9006ca694b9c
# change line 8: 7bb5379582fa463c
# change line 9: 5bfe4199d1a04f20
# change line 10: 8b6b99d3802e4207
# change line 11: 947e9125adc34a8e
# change line 12: 726815621d7b43a6
# change line 13: 077ae943c31d4c8a
# change line 14: 346bbf20c00c41e1
# change line 15: fdd6fa016a814087
# change line 16: 5956591bc72c44ea
# change line 17: dee5cd947bac4e46
# change line 18: 431879b3906a41f8
# change line 19: 51bf6dc93d314e35
# change line 20: 2c73f0326d834e59
# change line 21: 95f4bf647b94455c
# change line 22: 1fa6746ff56f40e2
# change line 23: e77a805a8a094ffc
# change line 24: f3fe8a82142645eb
# change line 25: 896a6d56468b4987
# change line 26: 8a50f8849a2243da
# change line 27: b3617aae5cc444ef
# change line 28: 10d660b56cc6475c
# change line 29: 23a1ced1d9da4dea
# change line 30: 7d3ff1b68f344882
# change line 31: 81e2f31de6a340f4
# change line 32: 4d4cb495e3c44890
# change line 33: 4bc379e53d474cd6
# change line 34: e59b78fc2df5411b
# change line 35: 2aa7fb7adffd44dd
# change line 36: 308d3b43eca34589
# change line 37: dd0b6eea773a4200
# change line 38: 704a20325428467b
# change line 39: 5904fbf228414e43
# change line 40: 29764cb0ce7e4558
# change line 41: 5cfefe36641a4725
# change line 42: ec94bcd45aaa4eeb
# change line 43: 39f6e69874394f6f
# change line 44: 03a67f2644fb4464
# change line 45: cb0a35eda523462e
# change line 46: de3316d7631b45cc
# change line 47: 6614a6c7a2544410
# change line 48: ccc4141bdc9143cd
# change line 49: c417846598274d7b
# change line 50: 85dc289e58664723
# change line 51: 19b625f1a8ea4ac2
# change line 52: 8aa96c10e49b4184
# change line 53: 84e7c1bfa9b04d47
# change line 54: 8d8384b085b84bae
# change line 55: 8db0e7df087141f6
# change line 56: a4251813f909477e
# change line 57: 1f7ba479894046e2
# change line 58: a3c42608382f482c
# change line 59: 6b557eae14674e0d
# change line 60: 45227579c6704d1d
# change line 61: dcc7a3d96a5c471b
# change line 62: 0622f67dee2e4f52
# change line 63: b17955423b9044d3
# change line 64: 40ed0ee17e7e4db1
# change line 65: acc4171833484598
# change line 66: e4f2b582084047eb
# change line 67: e4a15a0ab8eb45c7
# change line 68: fc360a31eeb44b45
# change line 69: 8d504d359094444b
# change line 70: e64ce1026ff24c2d
# change line 71: 5c1f66ee58ed4e55
# change line 72: 84253d3f2b5c41d1
# change line 73: 4345b28addb64d45
# change line 74: 7e9cf070310044c1
# change line 75: fdbee070fc9b4f65
# change line 76: c0c1c20ebbfe431c
# change line 77: 91c4a5620e9f4e33
# change line 78: e3d023fdd5754cf8
# change line 79: 59fa3e48b72f4fa6
# change line 80: d3d1cff6922b447d
# change line 81: 690a56f7716f45af
# change line 82: 4e1d0a4fd2944b31
# change line 83: b2928f72f0bc418c
# change line 84: d71454e142c34f45
# change line 85: 2fb4f63aa8934783
# change line 86: 33d24da1e10c49cf
# change line 87: 612e76c2acf14c5a
# change line 88: 1c3533c53a1d4ddb
