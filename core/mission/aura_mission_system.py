
from core.mission.aura_mission_manager import (

    AURAMissionManager

)

from core.scheduler.aura_task_scheduler import (

    AURATaskScheduler

)

from core.mission.aura_mission_executor import (

    AURAMissionExecutor

)

from core.mission.aura_mission_dispatcher import (

    AURAMissionDispatcher

)

class AURAMissionSystem:

    def __init__(

        self,

        bridge

    ):

        self.manager = AURAMissionManager()

        self.scheduler = AURATaskScheduler()

        self.executor = AURAMissionExecutor(

            self.manager,

            self.scheduler

        )

        self.dispatcher = AURAMissionDispatcher(

            self.scheduler,

            bridge

        )

    def create_mission(

        self,

        title,

        objective

    ):

        return self.manager.create(

            title,

            objective

        )

    def add_task(

        self,

        mission_id,

        agent,

        task

    ):

        return self.executor.assign(

            mission_id,

            agent,

            task

        )

    def run_next(self):

        return self.dispatcher.dispatch_next()

    def status(self):

        return {

            "missions": self.manager.list(),

            "tasks": self.scheduler.list(),

            "dispatches": self.dispatcher.get_history()

        }

