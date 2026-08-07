
from core.storage.aura_persistent_store import AURAPersistentStore

from core.scheduler.aura_task_scheduler import (

    AURATaskScheduler

)

class AURAMissionExecutor:

    def __init__(

        self,

        mission_manager,

        scheduler

    ):

        self.missions = mission_manager

        self.scheduler = scheduler
        self.storage = AURAPersistentStore()

    def assign(

        self,

        mission_id,

        agent,

        task

    ):

        scheduled = self.scheduler.schedule(

            mission_id,

            agent,

            task

        )

        self.missions.add_task(

            mission_id,

            scheduled

        )

        self.storage.add(

            "tasks",

            scheduled

        )

        return scheduled

    def start_mission(

        self,

        mission_id

    ):

        return self.missions.start(

            mission_id

        )

    def get_next(self):

        return self.scheduler.next_task()

