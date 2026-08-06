from datetime import datetime

from uuid import uuid4

class AgentRuntime:

    """

    Base runtime for AURA agents.

    """

    def __init__(

        self,

        name: str,

        capabilities: list,

        permissions: list

    ):

        self.id = str(uuid4())

        self.name = name

        self.capabilities = capabilities

        self.permissions = permissions

        self.memory = []

        self.tasks = []

    def can_execute(

        self,

        capability

    ):

        return capability in self.capabilities

    def remember(

        self,

        item

    ):

        self.memory.append(item)

    def execute(

        self,

        task,

        capability

    ):

        if not self.can_execute(capability):

            return {

                "status": "denied",

                "reason": "Capability unavailable"

            }

        result = {

            "agent": self.name,

            "task": task,

            "capability": capability,

            "status": "completed",

            "timestamp": datetime.utcnow().isoformat()

        }

        self.tasks.append(result)

        self.remember(result)

        return result