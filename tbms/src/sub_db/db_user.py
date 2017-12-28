"""
User subsystem specific database operations that the db_manager will call
"""

from db_def import User
from db_def import Credentials

from src.sub_db import Session

session = Session()


def create(item, val):
    """
    Insert the given item into the table with the given values.
    :param item: String specifying which object is being added to the database.
    :param val: Dictionary with the values that should be entered into the
    table.
    :return: Id number of the newly created object in the table.  If nothing
    was added to the database should return -1.
    """
    new_id = -1
    if item == "user":
        new_user = User(first_name = val['first_name'],
                        last_name = val['last_name'],
                        organization = val['organization'],
                        email = val['email'],
                        skill_level = val['skill_level'],
                        permissions = val['permissions'])
        session.add(new_user)
        session.commit()

        new_id = new_user.id

    elif item == "credentials":
        new_cred = Credentials(user_id = val['user_id'],
                               username = val['username'],
                               password = val['password'],
                               salt = val['salt'])

        session.add(new_cred)
        session.commit()

        new_id = new_cred.user_id

    return new_id


def read(item, item_id = None):
    """
    Retrieves the specified item with "item_id" from the database.
    :param item: String that specifies the object or query that is to be
    retrieved.
    :param item_id: Id number in the table of the entity
    :return: A dictionary, or list of dictionaries of the resulting query.
    If the item with the "item_id" was not found, return an empty dictionary
    """
    if item == "user":
        res = session.query(User).filter(User.id == item_id)
        user = user_to_dict(res)
        return user

    elif item == "credentials":
        res = session.query(Credentials).filter(Credentials.username == item_id)
        cred = credentials_to_dict(res)
        return cred

    elif item == "all users":
        res = session.query(User).all()
        users = []
        for u in res:
            users.append(user_to_dict(u))
        return users

    else:
        return dict()


def update(item, item_id, val):
    """

    :param item:
    :param item_id:
    :param val:
    :return:
    """
    status = False
    if item == "user":
        user = read("user", item_id)
        if 'first_name' in val:
            user.first_name = val['first_name']
        if 'last_name' in val:
            user.last_name = val['']
        if 'organization' in val:
            user.organization = val['organization']
        if 'email' in val:
            user.email = val['email']
        if 'skill_level' in val:
            user.skill_level = val['skill_level']
        if 'permissions' in val:
            user.permissions = val['permissions']
        if 'session_id' in val:
            user.session_id = val['session_id']

        session.commit()
        status = True

    elif item == "credentials":
        credentials = read("credentials", item_id)
        if 'username' in val:
            credentials.username = val['username']
        if 'password' in val:
            credentials.password = val['password']

        session.commit()

    return status


def delete(item, item_id):
    """

    :param item:
    :param item_id:
    :return:
    """
    status = False
    if item == "user":
        user = read("user", item_id)
        delete("credentials", item_id)
        session.delete(user)
        session.commit()
        status = True

    elif item == "credentials":
        credentials = read("credentials", item_id)
        session.delete(credentials)
        session.commit()
        status = True

    return status


def user_to_dict(obj):
    d = {'id': obj.id, 'first_name': obj.first_name, 'last_name': obj.last_name,
         'organization': obj.organization, 'email': obj.email,
         'skill_level': obj.skill_level, 'permissions': obj.permissions,
         'session_id': obj.session_id}

    return d


def credentials_to_dict(obj):
    d = {'username': obj.username, 'password': obj.password, 'salt': obj.salt}

    return d
