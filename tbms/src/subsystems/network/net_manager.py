"""
Interface for the network subsystem for the rest of the system
"""
import connection_string
from server import Server
import session
import statistics

def create():
    pass

# Return server instance or
# Return session instance or
# Return statistics instance or
# Return connection_string instance
def read(class_name):
    if class_name == 'servers': # Get all servers in database
        servers = []
        id = 1
        server = Server(id, '', '', [], [], [], [])
        servers.append(server.read())
        if id == -1:
            return None
        else:
            return servers
    elif class_name == 'session':
        pass
    elif class_name == 'statistics':
        pass
    elif class_name == 'connection_string':
        pass
    else:
        print("No such class in this subsystem!")


def update():
    pass


def delete():
    pass


def admin_session():
    pass
