"""
Network subsystem specific database operations that the db_manager will call
"""


def get(item, item_id):
    # Dictionary Stub
    dictionary = {}
    if item == "servers" and item_id == 1:
        dictionary = {
            'id': 1,
            'ip': "192.168.0.18",
            'username': "Vbox",
            'password': "password"
        }
    elif item == "servers" and item_id == 2:
        dictionary = {
            'id': 2,
            'ip': "Some ip",
            'username': "Some username",
            'password': "Some password"
        }
    return dictionary


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
