import base64

class EncryptionManager:

    """

    Foundation encryption manager for AURA.

    

    Note:

    This is a placeholder layer.

    Production AURA will use hardened

    cryptographic key management.

    """

    def __init__(self, key: str):

        self.key = key.encode()

    def encrypt(self, data: str) -> str:

        encoded = data.encode()

        encrypted = bytes(

            [

                byte ^ self.key[i % len(self.key)]

                for i, byte in enumerate(encoded)

            ]

        )

        return base64.b64encode(

            encrypted

        ).decode()

    def decrypt(self, encrypted_data: str) -> str:

        encrypted = base64.b64decode(

            encrypted_data

        )

        decrypted = bytes(

            [

                byte ^ self.key[i % len(self.key)]

                for i, byte in enumerate(encrypted)

            ]

        )

        return decrypted.decode()