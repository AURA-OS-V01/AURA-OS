from uuid import uuid4

class AURABusinessConnector:

    def __init__(self):

        self.business_systems = []

    def connect_business_tool(

        self,

        name,

        category

    ):

        tool = {

            "id":

                str(uuid4()),

            "name":

                name,

            "category":

                category,

            "status":

                "connected"

        }

        self.business_systems.append(tool)

        return tool

    def get_tools(self):

        return self.business_systems