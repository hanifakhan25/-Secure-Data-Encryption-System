# --- encryption_utils.py ---
import hashlib
from cryptography.fernet import Fernet

def create_fernet():
    return Fernet(Fernet.generate_key())

def hash_passkey(passkey: str) -> str:
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(fernet: Fernet, text: str) -> str:
    return fernet.encrypt(text.encode()).decode()

def decrypt_data(fernet: Fernet, encrypted_text: str, passkey: str, stored_data: dict):
    hashed = hash_passkey(passkey)
    match = stored_data.get(encrypted_text) or stored_data.get(passkey)
    if match and match['passkey'] == hashed:
        return fernet.decrypt(match['encrypted_text'].encode()).decode()
    return None