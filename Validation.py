import re

# Class used to create multiple methods for validating data input by user


class Validation:

    # Validates email
    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    # Validates name
    @staticmethod
    def validate_name(name):
        pattern = r"^[a-z0-9._]*$"
        return re.match(pattern, name) is not None

    # Validate username
    @staticmethod
    def validate_account(username):
        pattern = r"^[a-z0-9._]*$"
        return re.match(pattern, username) is not None

    # Validate password
    # The password must be at least eight characters long.
    # The password must contain at least one uppercase letter.
    # The password must contain at least one lowercase letter.
    # The password must contain at least one digit.

    @staticmethod
    def validate_password(password):
        pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
        return re.match(pattern, password) is not None
