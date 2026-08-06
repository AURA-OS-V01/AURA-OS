from uuid import uuid4

from datetime import datetime

class AURAStrategicPlanningEngine:

    def __init__(self):

        self.plans = []

    def create_plan(

        self,

        goal,

        description

    ):

        plan = {

            "id":

                str(uuid4()),

            "goal":

                goal,

            "description":

                description,

            "actions":

                [],

            "created":

                datetime.utcnow().isoformat()

        }

        self.plans.append(plan)

        return plan

    def add_action(

        self,

        plan_id,

        action,

        priority

    ):

        for plan in self.plans:

            if plan["id"] == plan_id:

                step = {

                    "action":

                        action,

                    "priority":

                        priority,

                    "status":

                        "pending"

                }

                plan["actions"].append(step)

                return step

        return None

    def generate_next_action(

        self,

        plan_id

    ):

        for plan in self.plans:

            if plan["id"] == plan_id:

                if not plan["actions"]:

                    return None

                return max(

                    plan["actions"],

                    key=lambda item:

                    item["priority"]

                )

        return None

    def get_plans(self):

        return self.plans