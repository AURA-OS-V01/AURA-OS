from uuid import uuid4

from datetime import datetime

class AURAAutonomousDecisionLayer:

    def __init__(self):

        self.decisions = []

        self.action_plans = []

    def analyze_situation(

        self,

        situation,

        impact

    ):

        if impact >= 80:

            priority = "high"

        elif impact >= 50:

            priority = "medium"

        else:

            priority = "low"

        decision = {

            "id":

                str(uuid4()),

            "situation":

                situation,

            "impact":

                impact,

            "priority":

                priority,

            "created":

                datetime.utcnow().isoformat()

        }

        self.decisions.append(

            decision

        )

        return decision

    def select_agent(

        self,

        decision

    ):

        if decision["priority"] == "high":

            agent = "enterprise_orchestrator"

        elif decision["priority"] == "medium":

            agent = "workflow_builder"

        else:

            agent = "analytics_engine"

        return agent

    def create_action_plan(

        self,

        decision,

        agent

    ):

        plan = {

            "id":

                str(uuid4()),

            "decision_id":

                decision["id"],

            "agent":

                agent,

            "status":

                "ready",

            "created":

                datetime.utcnow().isoformat()

        }

        self.action_plans.append(

            plan

        )

        return plan

    def get_decision_state(self):

        return {

            "decisions":

                self.decisions,

            "plans":

                self.action_plans

        }