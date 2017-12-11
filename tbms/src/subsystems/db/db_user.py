"""
User subsystem specific database operations that the db_manager will call
"""


def get(item, item_id):
    # Dictionary Stub
    dictionary = {}
    if item == "credentials" and item_id == "admin":
        dictionary = {
            'username': "admin",
            'password': "0f27103a56db6bbf781c1b5ea4c8d5dcb7448d6d6209c061de7057d915e1f7ee",
            'salt': "1d6442ddcfd9db1ff81df77cbefcd5afcc8c7ca952ab3101ede17a84b866d3f3",
            'id': 1234
        }
    elif item == "credentials" and item_id == "tech.kings2":
        dictionary = {
            'username': "tech.kings2",
            'password': "281582ce2c0fad4dd8bd10238ca934b95531511322b9cea1de8ecb6f2cbeaf97",
            'salt': "d72b06c7ebe1361c21454182f676f72cb0899ccf36903a23b67cecd167a2068d",
            'id': 1235
        }
    elif item == "credentials" and item_id == "tech.kings3":
        dictionary = {
            'username': "tech.kings3",
            'password': "afe8d7a9e0bf9c80ebf2c8f5a7e999f5ebe9ef74e2b57510038fc6d7f3fe8432",
            'salt': "95439dd70d46c990f352206bfc1e0ca713dc8a52103a159684cbdf5c8376e6c4",
            'id': 1236
        }
    elif item == "user" and item_id == 1234:
        dictionary = {
            'id': 1234,
            'first_name': "Admin",
            'last_name': "Istrator",
            'organization': "UTEP",
            'email': "aistrator@utep.edu",
            'skill_level': "advanced",
            'permission': 1
        }
    elif item == "user" and item_id == 1235:
        dictionary = {
            'id': 1235,
            'first_name': "Tech2",
            'last_name': "Kings2",
            'organization': "UTEP",
            'email': "tkings2@miners.utep.edu",
            'skill_level': "beginner",
            'permission': 2
        }
    elif item == "user" and item_id == 1236:
        dictionary = {
            'id': 1236,
            'first_name': "Tech3",
            'last_name': "Kings3",
            'organization': "ARL",
            'email': "tkings3@miners.utep.edu",
            'skill_level': "intermediate",
            'permission': 2
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
