"""
A server is where the entities created by the workshop subsystem will be
stored in order for them to be used by participants.
"""
from vboxapi import VirtualBoxManager

from ..db.db_manger import NetworkDB


class Server:
    """
    Representation of a server in the system.
    """

    def __init__(self, id, ip, username, password, status, groups, units, standalone_units, vms):
        self.id = id
        self.ip = ip
        self.username = username
        self.password = password
        self.status = status
        self.groups = groups
        self.units = units
        self.standalone_units = standalone_units
        self.vms = vms

    def create(self):
        pass

    def read(self):
        # return dictionary of server specified by the id
        dictionary = NetworkDB.get("servers", self.id)
        # get vm info
        manager = VirtualBoxManager("WEBSERVICE", {
            'url': 'http://'+dictionary['ip']+':18083/',
            'user': dictionary['username'],
            'password': dictionary['password']})

        # Get the global VirtualBox object
        vbox = manager.getVirtualBox()

        if len(dictionary.keys()) == 0:
            return None
        else:
            return Server(dictionary['id'], dictionary['ip'], dictionary['username'], dictionary['password'],
                          'N/A',
                          [],
                          [],
                          [],
                          [])

    def update(self):
        pass

    def delete(self):
        pass

    def get_ip(self):
        return self.ip

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_status(self):
        return self.status

    def get_groups(self):
        return self.groups

    def get_units(self):
        return self.units

    def get_standalone_units(self):
        return self.standalone_units

    def get_vms(self):
        return self.vms

    def set_vms(self, vm_list):
        self.vms = vm_list

    def print_server(self):
        print(str(self.id)+" "+str(self.ip)+" "+str(self.status)+" "+str(self.groups)+" "+str(self.units)+" "+str(self.standalone_units)+" "+str(self.vms))
    # not sure if there is anything else we need to add here
    # for private responsibilities. Store maybe?
