
from datetime import datetime, UTC

from core.agents.aura_agent_resolver import (

    AURAAgentResolver

)

from core.execution.aura_agent_executor import (

    AURAAgentExecutor

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

        self.executor = AURAAgentExecutor()

        self.history = []

    def dispatch_next(self):

        task = self.scheduler.next_task()

        if not task:

            return None

        agent = self.resolver.resolve(

            task["agent"]

        )

        execution = self.executor.execute(

            agent,

            task

        )

        result = {

            "task": task,

            "agent": agent,

            "execution": execution,

            "dispatched_at": datetime.now(

                UTC

            ).isoformat()

        }

        self.history.append(result)

        return result

    def get_history(self):

        return self.history

