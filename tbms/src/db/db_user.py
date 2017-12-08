"""
User subsystem specific database operations that the db_manager will call
"""


def get(item, item_id):
    # Dictionary Stub
    dictionary = {}
    if item == "credentials" and item_id == "tech.kings1":
        dictionary = {
            'username': "tech.kings1",
            'password': "fee156f9d7a9cf0dbfd5e4d8f6cfc64ff3afdcecba4fa0a3e19c730da9ec9617",
            'salt': "67b176705b46206614219f47a05aee7ae6a3edbe850bbbe214c536b989aea4d2",
            'id': 1234
        }
    elif item == "user" and item_id == 1234:
        dictionary = {
            'id': 1234,
            'first_name': "Tech",
            'last_name': "Kings",
            'organization': "UTEP",
            'email': "tkings@miners.utep.edu",
            'skill_level': "advanced",
            'permission': 1
        }
    """if item == "credentials" and item_id == "tech.kings2":
        dictionary = {
            'username': "tech.kings2",
            'password': "fee156f9d7a9cf0dbfd5e4d8f6cfc64ff3afdcecba4fa0a3e19c730da9ec9617",
            'salt': "67b176705b46206614219f47a05aee7ae6a3edbe850bbbe214c536b989aea4d2",
            'id': 1235
        }
    elif item == "user" and item_id == 1235:
        dictionary = {
            'id': 1235,
            'first_name': "Tech",
            'last_name': "Kings",
            'organization': "UTEP",
            'email': "tkings2@miners.utep.edu",
            'skill_level': "advanced",
            'permission': 2
        }"""
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
