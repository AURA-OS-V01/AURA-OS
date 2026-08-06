from datetime import datetime

from uuid import uuid4

class PlanningEngine:

    """

    Converts goals into structured plans.

    """

    def __init__(self):

        self.name = "AURA Planning Engine"

        self.plans = []

    def create_plan(

        self,

        goal: str,

        context: dict | None = None

    ):

        plan = {

            "id": str(uuid4()),

            "goal": goal,

            "context": context or {},

            "milestones": [],

            "tasks": [],

            "created": datetime.utcnow().isoformat()

        }

        self.plans.append(plan)

        return plan

    def add_milestone(

        self,

        plan_id: str,

        milestone: str

    ):

        for plan in self.plans:

            if plan["id"] == plan_id:

                plan["milestones"].append(

                    milestone

                )

                return True

        return False

    def add_task(

        self,

        plan_id: str,

        task: str

    ):

        for plan in self.plans:

            if plan["id"] == plan_id:

                plan["tasks"].append(

                    task

                )

                return True

        return False

    def get_plans(self):

        return self.plans