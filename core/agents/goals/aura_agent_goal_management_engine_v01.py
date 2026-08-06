from uuid import uuid4

from datetime import datetime

class AURAAgentGoalManagementEngine:

    def __init__(self):

        self.goals = []

    def create_goal(

        self,

        objective,

        category,

        priority

    ):

        goal = {

            "id": str(uuid4()),

            "objective": objective,

            "category": category,

            "priority": priority,

            "status": "active",

            "tasks": [],

            "created": datetime.utcnow().isoformat()

        }

        self.goals.append(goal)

        return goal

    def add_task(

        self,

        goal_id,

        task,

        capability

    ):

        for goal in self.goals:

            if goal["id"] == goal_id:

                task_item = {

                    "id": str(uuid4()),

                    "task": task,

                    "capability": capability,

                    "status": "pending"

                }

                goal["tasks"].append(task_item)

                return task_item

        return None

    def complete_task(

        self,

        goal_id,

        task_id

    ):

        for goal in self.goals:

            if goal["id"] == goal_id:

                for task in goal["tasks"]:

                    if task["id"] == task_id:

                        task["status"] = "completed"

                if goal["tasks"] and all(

                    task["status"] == "completed"

                    for task in goal["tasks"]

                ):

                    goal["status"] = "completed"

                return goal

        return None

    def get_goal_state(self):

        return {

            "goals": self.goals

        }