"""
Workshop subsystem specific operations that the db_manager will call.
"""

import q_workshops as q


def create(item, values):
    """
    :param item:
    :param values:
    :return:
    """
    if item == "virtual machine":
        q.add_vm(values)

    if item == "workshop unit":
        q.add_wu(values)

    if item == "workshop group":
        q.add_wg(values)

    if item == "snapshot":
        q.add_snapshot(values)

    if item == "network adapter":
        q.add_network_adapter(values)


def read(item, item_id=None):
    """

    :param item:
    :param item_id:
    :return:
    """
    if item == "virtual machine":
        return q.get_vm(item_id)

    if item == "workshop unit":
        return q.get_wu(item_id)

    if item == "workshop group":
        return q.get_wg(item_id)

    if item == "snapshot":
        return q.get_snapshot(item_id)

    if item == "network adapter":
        return q.get_network_adapter(item_id)

    if item == "all vms":
        return q.get_all_vms()

    if item == "all wus":
        return q.get_all_wus()

    if item == "all wgs":
        return q.get_all_wgs()

    if item == "server wus":
        return q.get_server_wus(item_id)

    if item == "server sawus":
        return q.get_server_standalone(item_id)

    if item == "server wgs":
        return q.get_server_wgs(item_id)


def update(item, item_id, values):
    """

    :param item:
    :param item_id:
    :param values:
    :return:
    """
    if item == "virtual machine":
        return q.update_vm(item_id, values)

    if item == "workshop unit":
        return q.update_wu(item_id, values)

    if item == "workshop group":
        return q.update_wg(item_id, values)

    if item == "snapshot":
        return q.update_wu(item_id, values)

    if item == "network adapter":
        return q.update_network_adapter(item_id, values)


def delete(item, item_id):
    """

    :param item:
    :param item_id:
    :return:
    """
    if item == "virtual machine":
        return q.delete_vm(item_id)

    if item == "workshop unit":
        return q.delete_wu(item_id)

    if item == "workshop group":
        return q.delete_wg(item_id)

    if item == "snapshot":
        return q.delete_snapshot(item_id)

    if item == "network adapter":
        return q.delete_network_adapter(item_id)