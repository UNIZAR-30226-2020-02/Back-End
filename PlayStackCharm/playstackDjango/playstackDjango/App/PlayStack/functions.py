import hashlib
from cryptography.fernet import Fernet
from Crypto.Cipher import AES


# Encripta cualquier texto pasado
# como cadena de bits
def encrypt(text):
    IV_SIZE = 16  # 128 bit, fixed for the AES algorithm
    KEY_SIZE = 32  # 256 bit meaning AES-256, can also be 128 or 192 bits
    SALT_SIZE = 16  # This size is arbitrary

    password = b'PlayStack'
    salt = b'\xa69r\x8d0\x1a\x0cX\x8a\xc4}\xe2\xc7\xb2T\xd9'
    derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000,
                                  dklen=IV_SIZE + KEY_SIZE)
    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]

    return salt + AES.new(key, AES.MODE_CFB, iv).encrypt(text)


# Desencripta un texto pasado como
# cadena de bitsencruptado
# por la funcion encrypt
def decrypt(text):
    IV_SIZE = 16  # 128 bit, fixed for the AES algorithm
    KEY_SIZE = 32  # 256 bit meaning AES-256, can also be 128 or 192 bits
    SALT_SIZE = 16  # This size is arbitrary

    password = b'PlayStack'
    salt = text[0:SALT_SIZE]
    derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000,
                                  dklen=IV_SIZE + KEY_SIZE)
    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]
    return AES.new(key, AES.MODE_CFB, iv).decrypt(text[SALT_SIZE:])