"""
Interface for the network subsystem for the rest of the system
"""
import connection_string
from server import Server
from ..db.db_manager import NetworkDB
import session
import statistics


def create(item, values):
    return NetworkDB.create(item, values)


# Return server(s) instance or
# Return session(s) instance or
# Return statistics(s) instance or
# Return connection_string(s) instance
def read(item):
    data = NetworkDB.read(item)
    return data


def update():
    pass


def delete():
    pass


def admin_session():
    pass


def convert_query_list_to_instance_list(server_query_list):
    servers = []
    for server in server_query_list:
        servers.append(Server(server.id, server.ip, server.username, server.password, server.status))
    return servers