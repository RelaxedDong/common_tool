import time
import jwt

secret = b'\x7d\xef\x87\xd5\xf8\xbb\xff\xfc\x80\x91\x06\x91\xfd\xfc\xed\x69'


def create_jwt_token(dict_data):
    dict_data['exp'] = int(time.time() + 432000)  # 5天过期
    encoded = jwt.encode(dict_data, secret, algorithm='HS256')
    return str(encoded, encoding='ascii')


def decode_jwt_token(encoded_str):
    return jwt.decode(encoded_str, secret, algorithm='HS256')