# utils/authentication.py
import hashlib

def hash_password(password: str) -> str:
    """Return a SHA-256 hashed password. For real use, consider bcrypt or passlib."""
    return hashlib.sha256(password.encode()).hexdigest()
