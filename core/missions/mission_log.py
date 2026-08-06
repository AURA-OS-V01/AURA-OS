from datetime import datetime

from uuid import uuid4

class MissionLog:

    """

    Records AURA missions and events.

    """

    def __init__(self):

        self.missions = []

    def create_mission(

        self,

        name: str,

        objective: str

    ):

        mission = {

            "id": str(uuid4()),

            "name": name,

            "objective": objective,

            "status": "started",

            "events": [],

            "created": datetime.utcnow().isoformat()

        }

        self.missions.append(mission)

        return mission

    def add_event(

        self,

        mission_id: str,

        event: str

    ):

        for mission in self.missions:

            if mission["id"] == mission_id:

                mission["events"].append({

                    "event": event,

                    "time": datetime.utcnow().isoformat()

                })

                return mission

        return None

    def complete_mission(

        self,

        mission_id: str,

        result: str

    ):

        for mission in self.missions:

            if mission["id"] == mission_id:

                mission["status"] = "completed"

                mission["result"] = result

                return mission

        return None

    def get_missions(self):

        return self.missions