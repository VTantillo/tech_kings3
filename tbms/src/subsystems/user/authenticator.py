"""
Used to authenticate the credentials of a user who tries to log in to the
system.
"""
import _pysha3
from ..db.db_manager import UserDB


def hash_function(password, salt1):
    # Hash input password with the salts
    salt2 = "55b375a6cbd41c044e0ef9b23853370304cde7cc70c49e895687fbbefd4878eb"  # SHA3-256 for tech.kings
    sha3_256 = _pysha3.sha3_256()
    password = salt1 + password + salt2
    sha3_256.update(password.encode())
    return sha3_256.hexdigest()


def authenticate(username, password):
    # Get credentials and check password
    dictionary = UserDB.read("credentials", username)
    print(dictionary.count())
    # If not empty dictionary then extract password and salt and compare
    if dictionary.count() != 0:
        hashed_password = hash_function(password, dictionary[0].salt)
        if hashed_password == dictionary[0].password:
            return dictionary[0].user_id
        else:
            return -1
    else:
        return -1


def reset_password():
    pass

# Other private responsibilities
