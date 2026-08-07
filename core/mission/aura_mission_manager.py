
from datetime import datetime, UTC

from uuid import uuid4

class AURAMissionManager:

    def __init__(self):

        self.missions = {}

    def create(

        self,

        title,

        objective,

        priority="normal"

    ):

        mission = {

            "id": str(uuid4()),

            "title": title,

            "objective": objective,

            "priority": priority,

            "status": "created",

            "tasks": [],

            "created": datetime.now(

                UTC

            ).isoformat()

        }

        self.missions[

            mission["id"]

        ] = mission

        return mission

    def add_task(

        self,

        mission_id,

        task

    ):

        self.missions[

            mission_id

        ]["tasks"].append(task)

    def start(

        self,

        mission_id

    ):

        self.missions[

            mission_id

        ]["status"] = "running"

        return self.missions[

            mission_id

        ]

    def complete(

        self,

        mission_id

    ):

        self.missions[

            mission_id

        ]["status"] = "completed"

        return self.missions[

            mission_id

        ]

    def list(self):

        return list(

            self.missions.values()

        )

