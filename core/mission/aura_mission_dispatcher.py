
from datetime import datetime, UTC

from core.agents.aura_agent_resolver import (

    AURAAgentResolver

)

class AURAMissionDispatcher:

    def __init__(

        self,

        scheduler,

        bridge

    ):

        self.scheduler = scheduler

        self.bridge = bridge

        self.resolver = AURAAgentResolver(

            bridge.lifecycle_manager

        )

        self.history = []

    def dispatch_next(self):

        task = self.scheduler.next_task()

        if not task:

            return None

        agent_name = task["agent"]

        agent = self.resolver.resolve(

            agent_name

        )

        result = {

            "task": task,

            "agent": agent,

            "dispatched_at": datetime.now(

                UTC

            ).isoformat()

        }

        self.history.append(result)

        return result

    def get_history(self):

        return self.history

