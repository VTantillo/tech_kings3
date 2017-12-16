"""
A virtual machine will be used by a participant to complete and exercise.  Can
belong to a unit.
"""

from cloneable import Cloneable


class VirtualMachine(Cloneable):
    """
    A virtual network adapter to connect VMs
    """

    def __init__(self, name, id, adapter, port, recent_snapshot, host_ip):
        self.name = name
        self.id = id
        self. adapter = adapter
        self.port = port
        self.recent_snapshot = recent_snapshot
        self. host_ip = host_ip

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_adapter(self):
        return self.adapter

    def get_port(self):
        return self.port

    def get_recent_snapshot(self):
        return self.recent_snapshot

    def get_host_ip(self):
        return self.host_ip
    # private responsibilities go here
    # need to put how to clone here too
