"""
A workshop group contains multiple workshop units of a specific exercise
"""

from cloneable import Cloneable
from portable import Portable


class WorkshopGroup(Cloneable, Portable):
    """
    A collection of WUs of a particular exercise
    """

    def __init__(self, id, name, description, status, lifetime, published_date, server_id):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.lifetime= lifetime
        self.published_date = published_date
        self.server_id = server_id

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
