"""
Network subsystem specific database operations that the db_manager will call
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.db_def import Server
from db.db_def import ServerCredentials
from db.db_def import Session
from db.db_def import ConnectionString
from db.db_def import Statistics


def get(item, item_id):
    """
    Description:
    :param item:
    :param item_id:
    :return:
    """
    pass


def add(item, values):
    """
    Description:
    :param item:
    :param values:
    :return:
    """
    pass


def update(item, item_id, values):
    """
    Description:
    :param item:
    :param item_id:
    :param values:
    :return:
    """
    pass


def delete(item, item_id):
    """
    Description:
    :param item:
    :param item_id:
    :return:
    """
    pass
