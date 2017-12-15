from db_demo import Server

from src.sub_db import Session

session = Session()


def add_server(val):
    new_server = Server(ip=val['ip'],
                        status=val['status'],
                        username=val['username'],
                        password=val['password'])
    session.add(new_server)
    session.commit()


def get_server(server_id):
    res = session.query(Server).filter(Server.id == server_id)
    return res


def get_all_servers():
    res = session.query(Server).all()
    return res


def update_server(server_id, val):
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


def delete_server(server_id):
    server = get_server(server_id)
    session.delete(server)
    session.commit()


def delete_all_servers():
    server = get_all_servers()
    session.delete(server)
    session.commit()
