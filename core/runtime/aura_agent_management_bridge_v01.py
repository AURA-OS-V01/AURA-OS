from datetime import datetime, UTC

class AURAAgentManagementBridge:

    def __init__(

        self,

        registry,

        lifecycle_manager

    ):

        self.registry = registry

        self.lifecycle_manager = lifecycle_manager

    def add_agent(

        self,

        name,

        capability

    ):

        module = self.registry.register(

            name,

            "agent",

            capability

        )

        agent = self.lifecycle_manager.register_agent(

            name,

            capability

        )

        return {

            "module": module,

            "agent": agent

        }

    def activate_agent(

        self,

        name

    ):

        return self.lifecycle_manager.activate_agent(

            name

        )

    def pause_agent(

        self,

        name

    ):

        return self.lifecycle_manager.pause_agent(

            name

        )

    def retire_agent(

        self,

        name

    ):

        return self.lifecycle_manager.retire_agent(

            name

        )

    def get_agent_status(

        self,

        name

    ):

        agent = self.lifecycle_manager.get_agent(

            name

        )

        module = self.registry.get_module(

            name

        )

        return {

            "agent": agent,

            "module": module,

            "checked_at": datetime.now(

                UTC

            ).isoformat()

        }