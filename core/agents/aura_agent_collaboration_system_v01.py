from uuid import uuid4

from datetime import datetime

class AURAAgentCollaborationSystem:

    """

    Manages communication between AURA agents.

    """

    def __init__(self):

        self.agents = []

        self.messages = []

        self.requests = []

    def register_agent(

        self,

        name,

        agent_type

    ):

        agent = {

            "id":

                str(uuid4()),

            "name":

                name,

            "type":

                agent_type,

            "status":

                "active",

            "created":

                datetime.utcnow().isoformat()

        }

        self.agents.append(agent)

        return agent

    def send_message(

        self,

        sender,

        receiver,

        message

    ):

        communication = {

            "id":

                str(uuid4()),

            "sender":

                sender,

            "receiver":

                receiver,

            "message":

                message,

            "timestamp":

                datetime.utcnow().isoformat()

        }

        self.messages.append(

            communication

        )

        return communication

    def create_agent_request(

        self,

        requesting_agent,

        target_agent,

        task

    ):

        request = {

            "id":

                str(uuid4()),

            "from":

                requesting_agent,

            "to":

                target_agent,

            "task":

                task,

            "status":

                "pending",

            "created":

                datetime.utcnow().isoformat()

        }

        self.requests.append(request)

        return request

    def update_request_status(

        self,

        request_id,

        status

    ):

        for request in self.requests:

            if request["id"] == request_id:

                request["status"] = status

                return request

        return None

    def get_messages(self):

        return self.messages

    def get_requests(self):

        return self.requests