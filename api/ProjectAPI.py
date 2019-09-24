from flask_restful import Resource
import logging as logger

class ProjectAPI(Resource):

    def get(self):

        logger.debug("Inside the post method of Task")

        projectDetails = {
             
                "owner" : "Harsham Sevak",
                "projectName" : "Simple Flask app for Docker container"
        }


        return projectDetails,200







