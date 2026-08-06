from uuid import uuid4

from datetime import datetime

class ResearchMode:

    """

    Manages research projects.

    """

    def __init__(self):

        self.projects = []

    def create_project(

        self,

        topic,

        research_type

    ):

        project = {

            "id": str(uuid4()),

            "topic": topic,

            "type": research_type,

            "sources": [],

            "status": "created",

            "created":

                datetime.utcnow().isoformat()

        }

        self.projects.append(

            project

        )

        return project