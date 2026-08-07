
from datetime import datetime, UTC

from uuid import uuid4

class AURAAgentExecutor:

    def __init__(

        self,

        memory_bridge=None

    ):

        self.results = []

        self.memory_bridge = memory_bridge

    def execute(

        self,

        agent,

        task

    ):

        result = {

            "id": str(uuid4()),

            "agent": agent["name"] if agent else None,

            "task": task["task"],

            "status": "completed",

            "output": (

                f"{agent['name']} completed: "

                f"{task['task']}"

            ) if agent else "No agent found",

            "created": datetime.now(

                UTC

            ).isoformat()

        }

        self.results.append(result)

        if self.memory_bridge:

            self.memory_bridge.record_execution(

                result

            )

        return result

    def history(self):

        return self.results

