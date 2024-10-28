import encryption_function as encryption


class EncryptionSystem:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.private_key = encryption.generate_private_key()

    def encrypt_username(self):
        self.username = encryption.encrypt(self.username, self.private_key)

    def encrypt_email(self):
        self.email = encryption.encrypt(self.email, self.private_key)

    def decrypt_username(self):
        self.username = encryption.decrypt(self.username, self.private_key)

    def decrypt_email(self):
        self.email = encryption.decrypt(self.email, self.private_key)


if __name__ == "__main__":
    es = EncryptionSystem(username="Test", email="Robert@Robert.Robert")
    es.encrypt_username()
    es.encrypt_email()
    print(es.email)
    print(es.username)
    es.decrypt_username()
    es.decrypt_email()
    print(es.email)
    print(es.username)
