from uuid import uuid4

from datetime import datetime

class AURAAgentCollaborationNetwork:

    def __init__(self):

        self.agents = {}

        self.messages = []

        self.tasks = []

    def register_agent(

        self,

        name,

        capability

    ):

        agent_id = str(uuid4())

        agent = {

            "id": agent_id,

            "name": name,

            "capability": capability,

            "status": "online",

            "created": datetime.utcnow().isoformat()

        }

        self.agents[agent_id] = agent

        return agent

    def communicate(

        self,

        sender_id,

        receiver_id,

        message

    ):

        communication = {

            "id": str(uuid4()),

            "sender": sender_id,

            "receiver": receiver_id,

            "message": message,

            "created": datetime.utcnow().isoformat()

        }

        self.messages.append(

            communication

        )

        return communication

    def assign_task(

        self,

        agent_id,

        task_name

    ):

        task = {

            "id": str(uuid4()),

            "agent_id": agent_id,

            "task": task_name,

            "status": "assigned",

            "created": datetime.utcnow().isoformat()

        }

        self.tasks.append(

            task

        )

        return task

    def get_state(self):

        return {

            "agents": list(self.agents.values()),

            "messages": self.messages,

            "tasks": self.tasks

        }