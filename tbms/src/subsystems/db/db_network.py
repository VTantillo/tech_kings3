"""
Network subsystem specific database operations that the db_manager will call
"""
import q_networks as q


def create(item, values):
    """
    :param item:
    :param values:
    :return:
    """
    if item == "server":
        q.add_server(values)

    if item == "connection string":
        # Call thing for connection string
        pass

    if item == "session":
        # Call thing for session
        pass

    if item == "statistics":
        # Call thing for statistics
        pass


def read(item, item_id):
    """
    :param item:
    :param item_id:
    :return:
    """
    if item == "server":
        return q.get_server(item_id)

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
        return q.get_all_servers()

    if item == "all sessions":
        pass

    if item == "all statistics":
        pass


def update(item, item_id, values):
    """
    :param item:
    :param item_id:
    :param values:
    :return:
    """
    if item == "server":
        q.update_server(item_id, values)

    if item == "connection string":
        # Call thing for connection string
        pass

    if item == "session":
        # Call thing for session
        pass

    if item == "statistics":
        # Call thing for statistics
        pass


def delete(item, item_id):
    """
    :param item:
    :param item_id:
    :return:
    """
    if item == "server":
        q.delete_server(item_id)

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
        q.delete_all_servers()