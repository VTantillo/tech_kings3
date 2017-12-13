"""
Interface for the user subsystem
"""
import authenticator
from user import User


def create():
    pass


def read():
    pass


def update():
    pass


def delete():
    pass


def authenticate(username, password):
    # Get id of user
    id = authenticator.authenticate(username, password)
    user = User(id, "", "", "", "", "", -1)
    # If authenticator.authenticate returns -1 then user not found
    if id == -1:
        return None
    else:
        return user.read()
