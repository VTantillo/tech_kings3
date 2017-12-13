"""class representing ReferenceMaterials"""
class referenceMaterial(object):

    def __init__(self, id, file):
        """Initialize/create a survey"""
        self.file = file
        self.id = id

    def __str__(self):
        """used for testing purposes"""
        return str(self.file)+" " + str(self.id)




