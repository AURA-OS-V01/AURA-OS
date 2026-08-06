from datetime import datetime

from uuid import uuid4

class CollaborationManager:

    """

    Coordinates multiple AURA agents

    working on the same mission.

    """

    def __init__(

        self,

        message_bus,

        workspace,

        result_exchange

    ):

        self.message_bus = message_bus

        self.workspace = workspace

        self.result_exchange = result_exchange

        self.missions = []

    def start_collaboration(

        self,

        mission_id: str,

        agents: list

    ):

        mission = {

            "id": str(uuid4()),

            "mission_id": mission_id,

            "agents": agents,

            "status": "active",

            "started": datetime.utcnow().isoformat()

        }

        self.missions.append(mission)

        return mission

    def submit_agent_result(

        self,

        agent,

        task,

        result,

        confidence

    ):

        return self.result_exchange.submit_result(

            agent,

            task,

            result,

            confidence

        )

    def notify_agent(

        self,

        sender,

        receiver,

        message

    ):

        return self.message_bus.send(

            sender,

            receiver,

            message

        )

    def get_missions(self):

        return self.missions