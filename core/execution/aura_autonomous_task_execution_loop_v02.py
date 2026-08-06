from datetime import datetime

from uuid import uuid4

class AURAAutonomousTaskExecutionLoop:

    def __init__(self):

        self.tasks = []

    def create_task(

        self,

        description,

        priority="normal"

    ):

        task = {

            "id": str(uuid4()),

            "description": description,

            "priority": priority,

            "status": "pending",

            "steps": [],

            "created": datetime.utcnow().isoformat()

        }

        self.tasks.append(task)

        return task

    def create_goal_task(

        self,

        description,

        priority="normal"

    ):

        return self.create_task(

            description,

            priority

        )

    def assign_step(

        self,

        task_id,

        step

    ):

        for task in self.tasks:

            if task["id"] == task_id:

                task["steps"].append({

                    "id": str(uuid4()),

                    "step": step,

                    "status": "pending"

                })

                return task

        return None

    def execute(

        self,

        task_id

    ):

        for task in self.tasks:

            if task["id"] == task_id:

                task["status"] = "executing"

                for step in task["steps"]:

                    step["status"] = "completed"

                task["status"] = "completed"

                task["completed"] = datetime.utcnow().isoformat()

                return task

        return None

    def execute_task(

        self,

        task_id

    ):

        return self.execute(task_id)

    def get_task_state(

        self

    ):

        return {

            "tasks": self.tasks

        }