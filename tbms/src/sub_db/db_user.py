"""
User subsystem specific database operations that the db_manager will call
"""

from db_demo import User
from db_demo import Credentials

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


def read(item, item_id):
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


def update(item, item_id, values):
    """

    :param item:
    :param item_id:
    :param values:
    :return:
    """
    if item == "user":
        q.update_user(item_id, values)

    if item == "credentials":
        q.update_credentials(item_id, values)


def delete(item, item_id):
    """

    :param item:
    :param item_id:
    :return:
    """
    if item == "user":
        q.delete_user(item_id)

    if item == "credentials":
        # We probably aren't ever going to use this... but it's here
        # for completeness :)
        q.delete_credentials(item_id)


def user_to_dict(obj):
    d = {'id': obj.id, 'first_name': obj.first_name, 'last_name': obj.last_name,
         'organization': obj.organization, 'email': obj.email,
         'skill_level': obj.skill_level, 'permissions': obj.permissions,
         'session_id': obj.session_id}

    return d


def credentials_to_dict(obj):
    d = {'username': obj.username, 'password': obj.password, 'salt': obj.salt}

    return d
