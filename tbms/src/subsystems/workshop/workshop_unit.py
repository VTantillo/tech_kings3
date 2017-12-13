"""
A workshop unit contains multiple virtual machines for a particular exercise
"""

from cloneable import Cloneable
from portable import Portable
from ..db.db_manager import NetworkDB

class WorkshopUnit(Cloneable, Portable):
    """
    A collection of VMs of a particular exercise
    """

    def __init__(self, id, name, description, session, status, lifetime, published_date, server_id, wg_id, vms=[]):
        self.id = id
        self.name = name
        self.description = description
        self.session = session
        self.status = status
        self.lifetime = lifetime
        self.published_date = published_date
        self.server_id = server_id
        self.host_ip = 'Could not retrieve'
        self.set_host_ip()
        self.wg_id = wg_id
        self.vms = vms
        self.number_of_vms = 0

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
