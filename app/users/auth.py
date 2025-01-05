import argon2
from argon2 import PasswordHasher


ph = PasswordHasher()



def get_password_hash(password: str) -> str:
    return ph.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    try:
        return ph.verify(hashed_password, plain_password)
    except argon2.exceptions.VerifyMismatchError:
        return False
    except argon2.exceptions.VerificationError:
        return False

