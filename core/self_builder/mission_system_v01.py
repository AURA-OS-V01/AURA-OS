from uuid import uuid4

from datetime import datetime

class MissionSystem:

    """

    Manages AURA internal development missions.

    """

    def __init__(self):

        self.missions = []

    def create_mission(

        self,

        goal

    ):

        mission = {

            "id": str(uuid4()),

            "goal": goal,

            "status": "created",

            "created":

                datetime.utcnow().isoformat()

        }

        self.missions.append(

            mission

        )

        return mission

    def update_status(

        self,

        mission_id,

        status

    ):

        for mission in self.missions:

            if mission["id"] == mission_id:

                mission["status"] = status

                return mission

        return None

    def list_missions(self):

        return self.missions