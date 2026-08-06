from datetime import datetime, UTC

from uuid import uuid4

class AURAActionExecutionEngine:

    def __init__(

        self,

        memory_store=None,

        event_bus=None

    ):

        self.memory = memory_store

        self.event_bus = event_bus

        self.actions = []

    def create_action(

        self,

        name,

        target,

        parameters=None

    ):

        action = {

            "id": str(uuid4()),

            "name": name,

            "target": target,

            "parameters": parameters or {},

            "status": "created",

            "created": datetime.now(UTC).isoformat()

        }

        self.actions.append(

            action

        )

        return action

    def execute(

        self,

        action_id

    ):

        for action in self.actions:

            if action["id"] == action_id:

                action["status"] = "completed"

                action["completed"] = datetime.now(

                    UTC

                ).isoformat()

                if self.event_bus:

                    self.event_bus.publish(

                        "action_completed",

                        action

                    )

                if self.memory:

                    self.memory.store(

                        "action_result",

                        action

                    )

                return action

        return None

    def get_action(

        self,

        action_id

    ):

        for action in self.actions:

            if action["id"] == action_id:

                return action

        return None

    def get_state(

        self

    ):

        return {

            "total_actions": len(

                self.actions

            ),

            "actions": self.actions

        }