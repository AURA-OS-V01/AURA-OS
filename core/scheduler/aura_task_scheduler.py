
from datetime import datetime, UTC

from uuid import uuid4

class AURATaskScheduler:

    def __init__(self):

        self.queue = []

    def schedule(

        self,

        mission_id,

        agent,

        task

    ):

        item = {

            "id": str(uuid4()),

            "mission": mission_id,

            "agent": agent,

            "task": task,

            "status": "queued",

            "created": datetime.now(

                UTC

            ).isoformat()

        }

        self.queue.append(item)

        return item

    def next_task(self):

        for item in self.queue:

            if item["status"] == "queued":

                item["status"] = "running"

                return item

        return None

    def complete(

        self,

        task_id

    ):

        for item in self.queue:

            if item["id"] == task_id:

                item["status"] = "completed"

                return item

        return None

    def list(self):

        return self.queue

