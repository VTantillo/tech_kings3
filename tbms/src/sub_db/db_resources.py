"""
Resource subsystem specific database operations that the db_manager will call
"""

import q_resources as q


def create(item, values):
    """
    :param item:
    :param values:
    :return:
    """
    if item == "reference material":
        q.add_reference_materials(values)

    if item == "survey":
        q.add_survey(values)


def read(item, item_id):
    """

    :param item:
    :param item_id:
    :return:
    """
    if item == "reference material":
        q.get_reference_materials(item_id)

    if item == "survey":
        q.get_survey(item_id)

    if item == "all surveys":
        q.get_all_surveys(item_id)

    if item == "all reference materials":
        q.get_all_reference_materials(item_id)


def update(item, item_id, values):
    """

    :param item:
    :param item_id:
    :param values:
    :return:
    """
    if item == "reference material":
        q.update_reference_materials(item_id, values)

    if item == "survey":
        q.update_surveys(item_id, values)


def delete(item, item_id):
    """

    :param item:
    :param item_id:
    :return:
    """
    if item == "reference material":
        q.delete_reference_materials(item_id)

    if item == "survey":
        q.delete_survey(item_id)

    if item == "all reference materials":
        q.delete_all_reference_materials()

    if item == "all surveys":
        q.delete_all_surveys()
