"""
Workshop subsystem specific operations that the db_manager will call.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.db_def import VirtualMachine
from db.db_def import WorkshopUnit
from db.db_def import WorkshopGroup
from db.db_def import Snapshot
from db.db_def import NetworkAdapter


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