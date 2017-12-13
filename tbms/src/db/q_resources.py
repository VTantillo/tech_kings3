from db.db_demo import ReferenceMaterial
from db.db_demo import Survey

from db import Session

session = Session()


def add_survey(val):
    new_survey = Survey(name=val['name'],
                        file_location=val['file_location'],
                        completed=val['completed'])
    session.add(new_survey)
    session.commit()


def add_reference_materials(val):
    new_reference_materials = ReferenceMaterial(
        name=val['name'],
        file_location=val['file_location'],
        type=val['type'])
    session.add(new_reference_materials)
    session.commit()


def get_survey(survey_id):
    res = session.query(Survey).filter(Survey.id == survey_id)
    return res


def get_reference_materials(ref_id):
    res = session.query(ReferenceMaterial).filter(
        ReferenceMaterial.id == ref_id)
    return res


def get_all_surveys():
    res = session.query(Survey).all()
    return res


def get_all_reference_materials():
    res = session.query(ReferenceMaterial).all()
    return res


def update_surveys(survey_id, val):
    survey = get_survey(survey_id)
    if 'name' in val:
        survey.name = val['name']
    if 'file_location' in val:
        survey.file_location = val['file_location']
    if 'completed' in val:
        survey.completed = val['completed']
    if 'user_id' in val:
        survey.user_id = val['user_id']

    session.commit()


def update_reference_materials(ref_id, val):
    ref_materials = get_reference_materials(ref_id)
    if 'name' in val:
        ref_materials.name = val['name']
    if 'file_location' in val:
        ref_materials.file_location = val['file_location']
    if 'type' in val:
        ref_materials.type = val['type']

    session.commit()


def delete_survey(survey_id):
    survey = get_survey(survey_id)
    session.delete(survey)
    session.commit()


def delete_reference_materials(ref_id):
    ref_mat = get_reference_materials(ref_id)
    session.delete(ref_mat)
    session.commit()


def delete_all_surveys():
    survey = get_all_surveys()
    session.delete(survey)
    session.commit()


def delete_all_reference_materials():
    ref_mat = get_all_reference_materials()
    session.delete(ref_mat)
    session.commit()
