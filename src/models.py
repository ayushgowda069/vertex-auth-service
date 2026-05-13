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

# vertexci-sim:b47dba28 t=1778700489
# change line 0: b5855b6232334c31
# change line 1: dbb5c0fb5b8c4665
# change line 2: 0ee8ae37bff84be1
# change line 3: 3aa799d801714746
# change line 4: eca47aa5ad6b42a6
# change line 5: fb1a1f43b9344296
# change line 6: a38136cfaf8d4b15
# change line 7: d7134e1437b9411e
# change line 8: 6023b2b28b3046bd
# change line 9: 572dc44406744e34
# change line 10: 0d44e4d5caff4982
# change line 11: 3c23f3ee7c6f4dea
# change line 12: 152c2937ccb24f17
# change line 13: 2592400b56b94974
# change line 14: a7eaae415aa74664
# change line 15: a4a134b9b5b74208
# change line 16: e9a781f499e04f9b
# change line 17: 84787b65a72b4286
# change line 18: 1cc9dddafdbe41d0
# change line 19: e4ab2c6195744c79
# change line 20: a1d5d16b5b284ecf
# change line 21: a9ab7555263e4734
# change line 22: 30dc24885f0040a8
# change line 23: 63a6cbde4a664151
# change line 24: 373dc7f08dd64071
# change line 25: 259dfdd71c5944d2
# change line 26: 930ac4ebc90744ca
# change line 27: 5420fc69fda84309
# change line 28: 2ba19587570e43bc
# change line 29: f98e2d560a274f5b
# change line 30: 5ef32f9eeade4ab3
# change line 31: 0d3539904e744eaf
# change line 32: 277c7bd39b1f46ba
# change line 33: c327dd2d2682435b
# change line 34: 9b5c14790ced4775
# change line 35: cf5ad61aac864783
# change line 36: 1b625435e43844d6
# change line 37: 4c3fb598a7174636
# change line 38: b4281203ade54fe9
# change line 39: 2eb74b2928994bc7
# change line 40: 386e376d6e8c42fc
# change line 41: c248f1162c5c4b59
# change line 42: ef78c31b57b24f1d
# change line 43: 30d402be6d9b4cfa
# change line 44: 56a70c32469d44ce
# change line 45: cd2d90aaea484002
# change line 46: 85934e1b43044f6f
# change line 47: 0fb2188beea44636
# change line 48: 74b765a87fb2465c
# change line 49: 9c51fbb3ce934123
# change line 50: 3537a2033e5a4cd2
# change line 51: a71b28f8af4c4755
# change line 52: 892bdfd4f02b4561
# change line 53: 4ecc4b0c27d1483c
# change line 54: 590818fe12304f9b
# change line 55: 6e22fead79f747c3
# change line 56: e2120f694d8c4465
# change line 57: a740fe1239ea4e40
# change line 58: 9ce22c294a494a5e
# change line 59: 660139ecd83c443f
# change line 60: a205c3db19c340d0
# change line 61: 94267a6a68b2412f
# change line 62: 987af6ff0e3842d3
# change line 63: 346592a3f08748e4
# change line 64: 244b80374b574f88
# change line 65: 746910acecf44de2
# change line 66: b6547b1297ca464b
# change line 67: 08b89e8cff4b4e93
# change line 68: 7bd0a6cb8b354551
# change line 69: 6d46c07782054251
# change line 70: d32d9cc8abdc4f85
# change line 71: b59f50b6910d42d9
# change line 72: 1786de6b76f04b9a
# change line 73: 25821cd611944ea9
# change line 74: 82ce2c52e7cf414a
# change line 75: 9f86dfc8a6414a9f
# change line 76: 415f1be67d7a4105
# change line 77: 642ca7665c0c419c
# change line 78: 76274ec61d204649
# change line 79: 6e638787b9264938
# change line 80: 8a5260f441d64696
# change line 81: 1a08581922374a49
# change line 82: 79052e0896464ed2
# change line 83: 8bb9cfd3dfd44d17
# change line 84: b9b0867a0e134079
# change line 85: b9b856fc9d884e70
# change line 86: 1b8d1cccf75c4bd3
# change line 87: cf09990daf484f03
# change line 88: 23abb144d9a14ea4
# change line 89: 93e3bb6a4c5244d0
# change line 90: fc883886e6b44900
# change line 91: ebf4095e00374f2a
# change line 92: ab712223272a48f7
# change line 93: ec4f21e938b3430b
# change line 94: 732cab82c5004883
# change line 95: 374e9d8e5e2548bf
# change line 96: 33123744a7f34fb5
# change line 97: 99feaacc20bf4e49
# change line 98: 9b04a73003204c69
# change line 99: fa682d1e9dd04098
# change line 100: d193686a29534e21
# change line 101: aaabe73e498f48e0
# change line 102: 2c5d301fa31e464f
# change line 103: 54151c862c5d44a0
# change line 104: 95100153a0ff41ca
# change line 105: 10827014adcc4c13
# change line 106: 9d50e723aa7f4481
# change line 107: 2ddbf0ed9d4a41cc
# change line 108: b153c66c9ac84694
# change line 109: 1b7f1333a7974331
# change line 110: b5ff30df719848d4
# change line 111: c8118e43ed2c43c6
# change line 112: cdc8b6d243b34e45
# change line 113: ee5af77ce1844c8f
# change line 114: ba1f177f5d8e4d16
# change line 115: 2a0c34d4ff594e4e
# change line 116: c62792ea1e0b4a25
# change line 117: a34873c246174ac1
# change line 118: 47953898c5fc4233
# change line 119: 8eb44a7d6fac49a9
# change line 120: bc657b1a61f44e5f
# change line 121: a80faf2796ee4acc
# change line 122: 162e41e6a3d94e76
# change line 123: a86565226805402d
# change line 124: bd42036375b44f5b
# change line 125: 67923420c2384873
# change line 126: 7aaf061280a3474a
# change line 127: e1a4a972c6284bbe
# change line 128: a151b6e57ec04020
# change line 129: 1b9b9c01b6d94209
# change line 130: d4598e89633944b7
