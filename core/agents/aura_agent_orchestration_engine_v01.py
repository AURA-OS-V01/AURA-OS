from datetime import datetime

from uuid import uuid4

from core.integration.pipeline.aura_goal_execution_pipeline_v01 import (

    AURAGoalExecutionPipeline,

)

class AURAAgentOrchestrationEngine:

    def __init__(self):

        self.pipeline = AURAGoalExecutionPipeline()

        self.agents = {}

        self.executions = []

    # --------------------------------------------------

    # Agent Registration

    # --------------------------------------------------

    def register_agent(

        self,

        name,

        capability

    ):

        agent = {

            "id": str(uuid4()),

            "name": name,

            "capability": capability,

            "status": "available",

            "created": datetime.utcnow().isoformat()

        }

        self.agents[name] = agent

        return agent

    # --------------------------------------------------

    # Goal Assignment

    # --------------------------------------------------

    def assign_goal(

        self,

        goal,

        priority="normal"

    ):

        workflow = self.pipeline.create_pipeline(

            goal,

            priority

        )

        execution = {

            "id": str(uuid4()),

            "goal": goal,

            "pipeline_id": workflow["id"],

            "status": "assigned",

            "assigned_agents": [],

            "created": datetime.utcnow().isoformat()

        }

        self.executions.append(

            execution

        )

        return execution

    # --------------------------------------------------

    # Legacy Compatibility

    # --------------------------------------------------

    def assign_task(

        self,

        task,

        agents

    ):

        execution = self.assign_goal(

            task,

            "normal"

        )

        execution["assigned_agents"] = agents

        return execution

    # --------------------------------------------------

    # Steps

    # --------------------------------------------------

    def add_execution_step(

        self,

        execution_id,

        step

    ):

        for execution in self.executions:

            if execution["id"] == execution_id:

                return self.pipeline.add_step(

                    execution["pipeline_id"],

                    step

                )

        return None

    # --------------------------------------------------

    # Execution

    # --------------------------------------------------

    def execute_goal(

        self,

        execution_id

    ):

        for execution in self.executions:

            if execution["id"] == execution_id:

                result = self.pipeline.execute_pipeline(

                    execution["pipeline_id"]

                )

                execution["status"] = "completed"

                execution["result"] = result

                return execution

        return None

    # Legacy Compatibility

    def execute_task(

        self,

        execution_id

    ):

        return self.execute_goal(

            execution_id

        )

    # --------------------------------------------------

    # State

    # --------------------------------------------------

    def get_state(

        self

    ):

        return {

            "agents": list(

                self.agents.values()

            ),

            "executions": self.executions,

            "pipeline": self.pipeline.get_state()

        }