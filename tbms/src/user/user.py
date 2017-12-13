from db.db_def import User

class UserManager:

    def auth(self,username, password):
        id = Authenticator.auth(username,password)
        return User.getUser(id)

class Authenticator:

    def auth(self,username,password):
        hash = hash(password)
        dic = DB.Manager.getUserCredentials(username)
        if("pass" in dic & dic['pass'] == hash):
            return dic['id']
        else:
            return none

class User:

    def getUser(self,id):
        DBManager.getUser(id)


class UserRegister:
    """
    This method recive all the information from the form to add a user
    and add it to the database.

    """


# def addUser(fname, lname, organization, email, skill_level, permission_ID):

def add_user():
    fname = "Luis"
    lname = "Romero"
    organization = "EPCC"
    email = "lgromero2"
    skill_level = "advance"
    permission_ID = "Admin"

    print(fname, lname, email, skill_level, permission_ID)


"""
This method is going to modify user information
"""


def modify_user():
    add_user.skill_level = "novice"
    print(add_user.skill_level)


def user_print():
    print(add_user.fname, add_user.skill_leve)


# addUser("Luis", "Romero", "EPCC", "lgromero2@miners.utep.edu", "Advance", permission_ID= "Admin")

add_user()
modify_user()
user_print()
