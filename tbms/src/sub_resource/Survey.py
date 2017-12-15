"""a class representing Surveys"""
class survey:
    def __init__(self , id , file  ):
        """Initialize a survey"""
        """id should be a number given to uniquely identify the survey"""
        self.file = file
        self.id = id
        self.complete = False

    def __str__(self):
        """used for testing purposes"""
        return str(self.file)+" " + str(self.id)+" " + str(self.complete)

    def uploadSurvey( id, user,completedFile ):
        """need to upload a complete survey to the Database"""

        """call database with user id"""
        print("uploaded with user ID "+str(user))
