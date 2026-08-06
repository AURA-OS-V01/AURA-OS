from datetime import datetime

from uuid import uuid4

from core.execution.aura_autonomous_task_execution_loop_v02 import (

    AURAAutonomousTaskExecutionLoop

)

class AURAGoalExecutionPipeline:

    def __init__(self):

        self.execution_loop = AURAAutonomousTaskExecutionLoop()

        self.pipelines = []

    def create_pipeline(

        self,

        goal,

        priority="normal"

    ):

        task = self.execution_loop.create_goal_task(

            goal,

            priority

        )

        pipeline = {

            "id": str(uuid4()),

            "goal": goal,

            "task_id": task["id"],

            "status": "initialized",

            "created": datetime.utcnow().isoformat()

        }

        self.pipelines.append(

            pipeline

        )

        return pipeline

    def add_step(

        self,

        pipeline_id,

        step

    ):

        for pipeline in self.pipelines:

            if pipeline["id"] == pipeline_id:

                return self.execution_loop.assign_step(

                    pipeline["task_id"],

                    step

                )

        return None

    def execute_pipeline(

        self,

        pipeline_id

    ):

        for pipeline in self.pipelines:

            if pipeline["id"] == pipeline_id:

                result = self.execution_loop.execute(

                    pipeline["task_id"]

                )

                pipeline["status"] = "completed"

                pipeline["result"] = result

                return pipeline

        return None

    def get_state(

        self

    ):

        return {

            "pipelines": self.pipelines,

            "execution": self.execution_loop.get_task_state()

        }