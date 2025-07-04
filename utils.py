import hashlib
import base64
from cryptography.fernet import Fernet

def generate_key(password: str) -> bytes:
    sha = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(sha)
