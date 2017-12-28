"""
Resource subsystem specific database operations that the db_manager will call
"""
from db_def import ReferenceMaterial
from db_def import Survey

from src.sub_db import Session

session = Session()


def create(item, values):
    """
    :param item:
    :param values:
    :return:
    """
    new_id = -1
    if item == "reference material":
        new_reference_materials = ReferenceMaterial(
            name = values['name'],
            file_location = values['file_location'],
            type = values['type'])
        session.add(new_reference_materials)
        session.commit()

        new_id = new_reference_materials.id

    elif item == "survey":
        new_survey = Survey(name = values['name'],
                            file_location = values['file_location'],
                            completed = values['completed'])
        session.add(new_survey)
        session.commit()

        new_id = new_survey.id

    return new_id


def read(item, item_id = None):
    """

    :param item:
    :param item_id:
    :return:
    """
    if item == "reference material":
        res = session.query(ReferenceMaterial).filter(
            ReferenceMaterial.id == item_id)
        reference = reference_materials_to_dict(res)
        return reference

    elif item == "survey":
        res = session.query(Survey).filter(Survey.id == item_id)
        survey = survey_to_dict(res)
        return survey

    elif item == "all surveys":
        res = session.query(Survey).all()
        surveys = []
        for s in res:
            surveys.append(survey_to_dict(s))
        return surveys

    elif item == "all reference materials":
        res = session.query(ReferenceMaterial).all()
        refs = []
        for r in res:
            refs.append(reference_materials_to_dict(r))
        return refs

    else:
        return dict()


def update(item, item_id, val):
    """

    :param item:
    :param item_id:
    :param val:
    :return:
    """
    status = False
    if item == "reference material":
        ref_materials = read("reference material", item_id)
        if 'name' in val:
            ref_materials.name = val['name']
        if 'file_location' in val:
            ref_materials.file_location = val['file_location']
        if 'type' in val:
            ref_materials.type = val['type']

        session.commit()
        status = True

    elif item == "survey":
        survey = read("survey", item_id)
        if 'name' in val:
            survey.name = val['name']
        if 'file_location' in val:
            survey.file_location = val['file_location']
        if 'completed' in val:
            survey.completed = val['completed']
        if 'user_id' in val:
            survey.user_id = val['user_id']

        session.commit()
        status = True

    return status


def delete(item, item_id):
    """

    :param item:
    :param item_id:
    :return:
    """
    status = False
    if item == "reference material":
        ref_mat = read("reference material", item_id)
        session.delete(ref_mat)
        session.commit()
        status = True

    elif item == "survey":
        survey = read("survey", item_id)
        session.delete(survey)
        session.commit()
        status = True

    elif item == "all reference materials":
        ref_mats = read("all reference materials")
        session.delete(ref_mats)
        session.commit()
        status = True

    elif item == "all surveys":
        surveys = read("all surveys")
        session.delete(surveys)
        session.commit()
        status = True

    return status


def reference_materials_to_dict(obj):
    d = {'id': obj.id, 'name': obj.name, 'file_location': obj.file_location,
         'type': obj.type}

    return d


def survey_to_dict(obj):
    d = {'id': obj.id, 'name': obj.name, 'file_location': obj.file_location,
         'completed': obj.completed, 'user_id': obj.user_id}

    return d

