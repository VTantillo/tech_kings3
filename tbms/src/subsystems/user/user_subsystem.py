import _pysha3

from ..db.db_manger import UserDB


class UserManager:

    @staticmethod
    def auth(username, password):
        # Get id of user
        id = Authenticator.auth(username, password)
        # If Authenticator.auth returns -1 then user not found
        if id == -1:
            return None
        else:
            return User.get_user(id)


class Authenticator:

    @staticmethod
    def hash_function(password, salt1):
        # Hash input password with the salts
        salt2 = "55b375a6cbd41c044e0ef9b23853370304cde7cc70c49e895687fbbefd4878eb"  # SHA3-256 for tech.kings
        sha3_256 = _pysha3.sha3_256()
        password = salt1 + password + salt2
        sha3_256.update(password.encode())
        return sha3_256.hexdigest()

    @staticmethod
    def auth(username, password):
        # Get credentials and check password
        dictionary = UserDB.get("credentials", username)
        # If empty dictionary then record not found
        if len(dictionary.keys()) != 0:
            hashed_password = Authenticator.hash_function(password, dictionary['salt'])
            if hashed_password == dictionary['password']:
                return dictionary['id']
            else:
                return -1
        else:
            return -1


class User:
    def __init__(self, first_name, last_name, organization, email, skill_level, permission):
        self.first_name = first_name
        self.last_name = last_name
        self.organization = organization
        self.email = email
        self.skill_level = skill_level
        self.permission = permission

    @staticmethod
    def get_user(id):
        # return instance of user specified by the id
        dictionary = UserDB.get("user", id)
        if len(dictionary.keys()) == 0:
            return None
        else:
            return User(dictionary['first_name'], dictionary['last_name'], dictionary['organization'],
                        dictionary['email'],
                        dictionary['skill_level'], dictionary['permission'])

    def get_permissions(self):
        return self.permission
