from ReferenceMaterial import referenceMaterial
from Survey import survey

"""this class should handle all delegation of the resources
including the reference materials and surveys"""\
"""handles resources"""
def signalCRD_item(item, id ,value, file= '' ):
    """meant to delegate the CRUD ops of survey and ref to
    respective classes """
    print("calling signal crd")

    if item == "Survey":
        if value == 1:
            """create should signal database"""
            temp = survey(id,file)
            return temp

        elif value == 2:
            """Getter for survey should return survey from a database then create it."""
            print("get from database "+item)
        elif value ==3:
            """delete survey"""
            print("signaled delete "+item)
           ## survey.deleteSurvey(id)

    elif item == "ReferenceMaterial":

        if value == 1:
            "Create should signal database"
            temp = referenceMaterial(id,file)
            return temp

        elif value == 2:
            """Getter for refMat, will signal database"""
            print("database signaled "+item)

        elif value == 3:
            """delete reference and signal database"""
            print("signaled delete"+item)
           ## referenceMaterial.deleteReferenceMaterial(id)

def signalUpload(SurveyId, user, completedFile):
    """needs to signal database"""
    survey.uploadSurvey(SurveyId, user , completedFile)
