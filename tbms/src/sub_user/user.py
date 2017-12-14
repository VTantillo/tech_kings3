"""
A user of the system that has permissions, and may have other information about
them.
"""
from src.sub_db.db_manager import UserDB


class User:
    """
    A user of the system.
    """

    def __init__(self, user_id, first_name, last_name, organization, email, skill_level, permission):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.organization = organization
        self.email = email
        self.skill_level = skill_level
        self.permission = permission


    def create(self):
        pass

    def read(self):
        # return instance of user specified by the id
        dictionary = UserDB.read("user", self.user_id)
        if dictionary.count() == 0:
            return None
        else:
            return User(dictionary[0].id, dictionary[0].first_name,
                        dictionary[0].last_name, dictionary[0].organization,
                        dictionary[0].email, dictionary[0].skill_level,
                        dictionary[0].permissions)

    def update(self):
        pass

    def delete(self):
        pass

    def get_permissions(self):
        return self.permission

    # private responsibilities go here
