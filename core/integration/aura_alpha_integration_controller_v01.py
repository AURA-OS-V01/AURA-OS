from datetime import datetime

from uuid import uuid4

from core.runtime.aura_unified_intelligence_runtime_v01 import (

    AURAUnifiedIntelligenceRuntime,

)

from core.agents.goals.aura_agent_goal_management_engine_v01 import (

    AURAAgentGoalManagementEngine,

)

class AURAAlphaIntegrationController:

    def __init__(self):

        self.runtime = AURAUnifiedIntelligenceRuntime()

        self.goal_engine = AURAAgentGoalManagementEngine()

        self.workflows = []

    def start_workflow(

        self,

        objective,

        category="General",

        priority="normal"

    ):

        goal = self.goal_engine.create_goal(

            objective,

            category,

            priority

        )

        workflow = {

            "id": str(uuid4()),

            "goal_id": goal["id"],

            "objective": objective,

            "status": "initialized",

            "created": datetime.utcnow().isoformat()

        }

        self.workflows.append(workflow)

        return workflow

    def register_runtime_module(

        self,

        name,

        capability

    ):

        return self.runtime.register_module(

            name,

            capability

        )

    def execute_workflow(

        self,

        workflow_id

    ):

        for workflow in self.workflows:

            if workflow["id"] == workflow_id:

                execution = self.runtime.execute_pipeline(

                    workflow["objective"],

                    [

                        module["name"]

                        for module in self.runtime.modules.values()

                    ]

                )

                workflow["status"] = "completed"

                workflow["execution"] = execution

                return workflow

        return None

    def get_state(self):

        return {

            "workflows": self.workflows,

            "runtime": self.runtime.get_runtime_state(),

            "goals": self.goal_engine.get_goal_state()

        }