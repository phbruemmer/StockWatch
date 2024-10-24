import base64
import os


class EncryptionSystem:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.private_key = base64.urlsafe_b64encode(os.urandom(32))

    def generate_private_key(self):
        self.private_key = base64.urlsafe_b64encode(os.urandom(32))

    def encrypt_username(self):
        pass


if __name__ == "__main__":
    es = EncryptionSystem(username="Test", email="Robert@Robert.Robert")
    print(es.private_key)
