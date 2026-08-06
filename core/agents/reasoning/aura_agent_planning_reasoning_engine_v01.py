from datetime import datetime

from uuid import uuid4

class AURAAgentPlanningReasoningEngine:

    def __init__(self):

        self.plans = []

    def create_plan(

        self,

        objective,

        priority="normal"

    ):

        plan = {

            "id": str(uuid4()),

            "objective": objective,

            "priority": priority,

            "steps": [],

            "status": "created",

            "created": datetime.utcnow().isoformat()

        }

        self.plans.append(

            plan

        )

        return plan

    def add_step(

        self,

        plan_id,

        step,

        agent=None

    ):

        for plan in self.plans:

            if plan["id"] == plan_id:

                plan["steps"].append({

                    "id": str(uuid4()),

                    "step": step,

                    "agent": agent,

                    "status": "pending"

                })

                return plan

        return None

    def execute_plan(

        self,

        plan_id

    ):

        for plan in self.plans:

            if plan["id"] == plan_id:

                for step in plan["steps"]:

                    step["status"] = "completed"

                plan["status"] = "completed"

                plan["completed"] = datetime.utcnow().isoformat()

                return plan

        return None

    def reason(

        self,

        objective

    ):

        text = objective.lower()

        steps = []

        if "build" in text:

            steps.extend([

                "Analyze requirements",

                "Create implementation plan",

                "Assign execution agents",

                "Validate result"

            ])

        elif "research" in text:

            steps.extend([

                "Collect information",

                "Analyze findings",

                "Generate report"

            ])

        else:

            steps.extend([

                "Understand objective",

                "Create solution path",

                "Execute actions"

            ])

        return steps

    def get_state(

        self

    ):

        return {

            "plans": self.plans

        }