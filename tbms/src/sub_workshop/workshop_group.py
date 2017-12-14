"""
A workshop group contains multiple workshop units of a specific exercise
"""

from cloneable import Cloneable
from portable import Portable
from src.sub_db.db_manager import NetworkDB


class WorkshopGroup(Cloneable, Portable):
    """
    A collection of WUs of a particular exercise
    """

    def __init__(self, id, name, description, status, lifetime, published_date, server_id, wus=[]):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.lifetime= lifetime
        self.published_date = published_date
        self.server_id = server_id
        self.host_ip = 'Could not retrieve'
        self.set_host_ip()
        self.wus = wus
        self.number_of_wus = 0

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    # private responsibilities go here
    # clone and port stuff here too

    def set_host_ip(self):
        server = NetworkDB.read("server", self.server_id)
        self.host_ip = server[0].ip
