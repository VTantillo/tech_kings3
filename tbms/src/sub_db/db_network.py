"""
Network subsystem specific database operations that the db_manager will call
"""
from db_def import Server
from db_def import ServerCredentials
from db_def import ConnectionString
from db_def import Session
from db_def import Statistics

from src.sub_db import Session

session = Session()


def create(item, val):
    """
    :param item:
    :param val:
    :return:
    """
    if item == "server":
        new_server = Server(ip = val['ip'],
                            status = val['status'],
                            username = val['username'],
                            password = val['password'])
        session.add(new_server)
        session.commit()

    if item == "connection string":
        # Call thing for connection string
        pass

    if item == "session":
        # Call thing for session
        pass

    if item == "statistics":
        # Call thing for statistics
        pass


def read(item, item_id = None):
    """
    :param item:
    :param item_id:
    :return:
    """
    if item == "server":
        res = session.query(Server).filter(Server.id == server_id)
        return res

    if item == "connection string":
        # Call thing for connection string
        pass

    if item == "session":
        # Call thing for session
        pass

    if item == "statistics":
        # Call thing for statistics
        pass

    if item == "all servers":
        res = session.query(Server).all()
        return res

    if item == "all sessions":
        pass

    if item == "all statistics":
        pass


def update(item, item_id, val):
    """
    :param item:
    :param item_id:
    :param values:
    :return:
    """
    if item == "server":
        server = get_server(server_id)
        if 'ip' in val:
            server.ip = val['ip']
        if 'status' in val:
            server.status = val['status']
        if 'username' in val:
            server.username = val['username']
        if 'password' in val:
            server.password = val['password']

        session.commit()

    if item == "connection string":
        # Call thing for connection string
        pass

    if item == "session":
        # Call thing for session
        pass

    if item == "statistics":
        # Call thing for statistics
        pass


def delete(item, item_id = None):
    """
    :param item:
    :param item_id:
    :return:
    """
    if item == "server":
        server = get_server(server_id)
        session.delete(server)
        session.commit()

    if item == "connection string":
        # Call thing for connection string
        pass

    if item == "session":
        # Call thing for session
        pass

    if item == "statistics":
        # Call thing for statistics
        pass

    if item == "all servers":
        server = get_all_servers()
        session.delete(server)
        session.commit()
