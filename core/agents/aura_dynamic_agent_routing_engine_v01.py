from uuid import uuid4

from datetime import datetime

class AURADynamicAgentRoutingEngine:

    """

    Automatically selects agents based on requests.

    """

    def __init__(self):

        self.agent_map = {

            "coding": "Coding Agent",

            "research": "Research Agent",

            "analysis": "Analysis Agent",

            "writing": "Writing Agent",

            "planning": "Planning Agent"

        }

        self.routes = []

    def analyze_request(

        self,

        request

    ):

        selected = []

        text = request.lower()

        for keyword, agent in self.agent_map.items():

            if keyword in text:

                selected.append(agent)

        if not selected:

            selected.append(

                "Planning Agent"

            )

        route = {

            "id": str(uuid4()),

            "request": request,

            "agents": selected,

            "status": "routed",

            "created":

                datetime.utcnow().isoformat()

        }

        self.routes.append(route)

        return route

    def get_routes(self):

        return self.routes