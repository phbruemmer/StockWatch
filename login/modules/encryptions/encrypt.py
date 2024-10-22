class EncryptionSystem:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def encrypt_username(self):
        username_len = len(self.username)
        for i in range(0, username_len):
            print(self.username[i])


if __name__ == "__main__":
    es = EncryptionSystem(username="Robert", email="Robert@Robert.Robert")
    es.encrypt_username()