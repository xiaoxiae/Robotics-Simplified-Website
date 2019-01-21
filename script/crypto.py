"""A few simple cryptographic functions to provide protection for things like
API tokens, IPs, etc."""

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64


def _plaintext_to_key(password):
    """Converts a byte object of any size to a base64 url-safe password using
    SHA256 (taken from https://github.com/NikolaiT)."""
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password)
    return base64.urlsafe_b64encode(digest.finalize())


def encrypt(key, text):
    """Turns a plain byte object into an encrypted one using AES."""
    return Fernet(_plaintext_to_key(key)).encrypt(text)


def decrypt(key, encoded_text):
    """Turns an encrypted byte object into a plain one using AES."""
    return Fernet(_plaintext_to_key(key)).decrypt(encoded_text)