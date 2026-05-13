from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: str
    password: str
    full_name: Optional[str] = None


class UserLogin(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserOut(BaseModel):
    email: str
    role: str

# vertexci-sim:ab4b1104 t=1778684305
# change line 0: b2880ae400d14e88
# change line 1: 20e4581dd56d433c
# change line 2: 8e4c894c199844a5
# change line 3: 6b4695bb07b04b57
# change line 4: 643a7837bbe3488e
# change line 5: 997953c91d644eec
# change line 6: 68f9132044424499
# change line 7: 52d892d33cd94d24
# change line 8: 61cb87252a2145fd
# change line 9: d2c6493696424973
# change line 10: 69d1535bd67c4e08
# change line 11: c066eb60b4c340ca
# change line 12: 9bfabf409de344f1
# change line 13: 9448bba213234ec5
# change line 14: a8385198f4114f3f
# change line 15: 8101ad8169324bf9
# change line 16: 76d62ff7f46a43a3
# change line 17: 38a7e5d516d2413a
# change line 18: bb91a62cce9d46f4
# change line 19: a298f442baf6460e
# change line 20: c9acb60f1d4d4503
# change line 21: f285fd87069042a8
# change line 22: 4599eb517d814f84
# change line 23: d40230ac17ad4e40
# change line 24: 7b0968e868ac4d7e
# change line 25: 77344781b32d4d28
# change line 26: f1afb0a128df47c4
# change line 27: 284e3258d8ac4e77
# change line 28: d0cd6be9a95743f5
# change line 29: 6761f6d77d564fc0
# change line 30: 0012a2048f854985
# change line 31: 963bfb5b85ed4e5a
# change line 32: 70b6b16b71da4dff
# change line 33: 4cf8b2a2ae764851
# change line 34: 7437d7c78bd74f9c
# change line 35: 57214e72efe8411a
# change line 36: cd139063a4014755
# change line 37: ab1607171f88474a
# change line 38: bfbf64e2cb424630
# change line 39: 06253a6c49334813
# change line 40: e12ea2c421b64c71
# change line 41: 70de1df7d1a74259
# change line 42: 92838e98895b4211
# change line 43: 8295f16cb5bf4861
# change line 44: e7c08a2312b24c68
# change line 45: c9331e2f832f441b
# change line 46: b60a502a534743b2
# change line 47: 615344f6573a4a93
# change line 48: a49f778a89444aee
# change line 49: ee24447b1c4a4505
# change line 50: a5b058937c6b4e24
# change line 51: ef7b27e4877c4e0b
# change line 52: 528b67fc32574663
# change line 53: 429a36bf28224724
# change line 54: c6097bd668e54b9d
# change line 55: f785be6906404ed9
# change line 56: 5e275f2129d74739
# change line 57: 32b9b70310b34ce7
# change line 58: 02343917d75742b2
# change line 59: 53adf3dab2b44af0
# change line 60: 75d6197e04c94f4c
# change line 61: c633981f950245ac
# change line 62: 6bceff8e39b34320
# change line 63: fd80ac4df46f4cc2
# change line 64: ff3358736bba407f
# change line 65: 4eeff738f83244b9
# change line 66: c66e302e70344b3e
# change line 67: c95ce2accbaa4721
# change line 68: 3221fdee46104687
# change line 69: 0c2ea639c9904b5a
# change line 70: 5794ccbadcfa4478
# change line 71: 7090a1392162417a
# change line 72: d9d88a4ef7f34760
# change line 73: 94d3872822f64b37
# change line 74: 55a00b8868a34414
# change line 75: 68f35559f7b4400a
# change line 76: 39a9ab53526c4fa7
# change line 77: 286b29e455f14807
# change line 78: 5d6e6d1a615247af
# change line 79: 7b3a031343c24c1e
# change line 80: b0e33a0132f04a07
# change line 81: 920fbc1a552a40ab
# change line 82: efa772bb3bdc4cbb
# change line 83: ac740fdec8d647d3
# change line 84: d3b24302f4684968
# change line 85: 63b3a094731345d5
# change line 86: 1926cebc3d234b9f
# change line 87: 358d8fa6296f4939
# change line 88: 38380a6ab9cf4760
# change line 89: 2d3b02e63941456b
# change line 90: 5af478b94c6b4b35
# change line 91: 84879c768aba4a54
# change line 92: c56687c2b24c4deb
# change line 93: 640b924969244c6b
# change line 94: c3e225bf619e41d2
# change line 95: aeca538641444b3c
# change line 96: 248890bdb8974f8c
# change line 97: e120aac582e24240
# change line 98: e871911283104c48
# change line 99: e8ef8a343bc24d26
# change line 100: 279e221d37b34f4f
# change line 101: 6735f49508624ab7
# change line 102: 91e42e66e2b14617
# change line 103: c9f55236a00c443c
# change line 104: ba82704278ef4e10
# change line 105: ae72a097acf14f06
# change line 106: fbab115ce2f34f9f
# change line 107: 3740131fc16a4950
# change line 108: e7ba2fc47f2e4a75
# change line 109: fb77637a30b340f9
# change line 110: c48b8ebb09f241e8
# change line 111: e2287d56708e407f
# change line 112: 9e2bc2e855904ad8
# change line 113: f01982c7b00c4175
# change line 114: 7bcba93095bb4c1a
# change line 115: d54ccc514c764491
# change line 116: 8ac8dd76a2ef4943
# change line 117: bc795f8f35744a51
# change line 118: 00777f74f20c4f4c
# change line 119: 32c2ad939b304493
# change line 120: 5b8910c3bf274755
# change line 121: a1716bdc10ea4fbf
# change line 122: 5c56337a5031434c
# change line 123: 5c159d3a6ef84560
# change line 124: 61af290e330d4d48
# change line 125: dec8995159094931
# change line 126: 8ad260bc36b94894
# change line 127: 62dde19b826f465e
# change line 128: a4b013ea19054c31
# change line 129: 02190fe7411f45d4
# change line 130: 4ece9c1bb94e4eba
# change line 131: 87d54b5bd6164fa9
# change line 132: a4e69f0925e64e52
# change line 133: b235c058d8044493
# change line 134: 0cf1fcd1815342de
# change line 135: 50aca0abb95d4429
# change line 136: fb3915301b7b455a
# change line 137: 37847b1569fd4048
# change line 138: 634a75ae86914d0d
# change line 139: 98f476ed347d42de
# change line 140: 708aab2e2b1d405b
# change line 141: 978d54b241de4577
# change line 142: 269bdcced14d427b
# change line 143: 544674b317aa4d4c
# change line 144: 259c81a6c9a84485
# change line 145: ca24de1b1c65457f
