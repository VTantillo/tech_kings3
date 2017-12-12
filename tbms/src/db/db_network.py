"""
Network subsystem specific database operations that the db_manager will call
"""
from db import Session

session = Session


def create(item, values):
    """
    :param item:
    :param values:
    :return:
    """
    if item == "server":
        # Call thing for server
        pass

    if item == "connection string":
        # Call thing for connection string
        pass

    if item == "session":
        # Call thing for session
        pass

    if item == "statistics":
        # Call thing for statistics
        pass


def read(item, item_id):
    """

    :param item:
    :param item_id:
    :return:
    """
    if item == "server":
        # Call thing for server
        pass

    if item == "connection string":
        # Call thing for connection string
        pass

    if item == "session":
        # Call thing for session
        pass

    if item == "statistics":
        # Call thing for statistics
        pass

    if item == "all servers":
        pass

    if item == "all connection strings":
        pass

    if item == "all sessions":
        pass

    if item == "all statistics":
        pass


def update(item, item_id, values):
    """

    :param item:
    :param item_id:
    :param values:
    :return:
    """
    if item == "server":
        # Call thing for server
        pass

    if item == "connection string":
        # Call thing for connection string
        pass

    if item == "session":
        # Call thing for session
        pass

    if item == "statistics":
        # Call thing for statistics
        pass


def delete(item, item_id):
    """

    :param item:
    :param item_id:
    :return:
    """
    if item == "server":
        # Call thing for server
        pass

    if item == "connection string":
        # Call thing for connection string
        pass

    if item == "session":
        # Call thing for session
        pass

    if item == "statistics":
        # Call thing for statistics
        pass
