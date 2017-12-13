"""
User subsystem specific database operations that the db_manager will call
"""

import db.q_users as q


def create(item, values):
    """
    Insert the given item into the table with the given values.
    :param item:
    :param values:
    :return:
    """
    if item == "user":
        q.add_user(values)

    if item == "credentials":
        q.add_credentials(values)


def read(item, item_id):
    """

    :param item:
    :param item_id:
    :return:
    """
    if item == "user":
        q.get_user(item_id)

    if item == "credentials":
        q.get_credentials(item_id)

    if item == "all users":
        q.get_all_users()


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
