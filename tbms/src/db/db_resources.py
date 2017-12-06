"""
Resource subsystem specific database operations that the db_manager will call
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.db_def import ReferenceMaterial
from db.db_def import Survey


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
