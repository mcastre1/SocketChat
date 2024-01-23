import hashlib


class Hash:
    @staticmethod
    def hash_sha256(password):
        # Choosing a secure hashing algorithm, in this case SHA-256
        hash_algorithm = hashlib.sha256()

        # Encoding the password as bytes before hashing
        password_bytes = password.encode('utf-8')

        # Update the hash object with the password bytes
        hash_algorithm.update(password_bytes)

        # Get the hexadecimal representation of the hashed password
        hashed_password = hash_algorithm.hexdigest()

        return hashed_password
