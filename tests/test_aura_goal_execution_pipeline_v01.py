from core.integration.pipeline.aura_goal_execution_pipeline_v01 import (

    AURAGoalExecutionPipeline

)

def test_goal_execution_pipeline():

    pipeline = AURAGoalExecutionPipeline()

    result = pipeline.create_pipeline(

        "Build enterprise automation platform",

        "high"

    )

    pipeline.add_step(

        result["id"],

        "Create architecture"

    )

    completed = pipeline.execute_pipeline(

        result["id"]

    )

    state = pipeline.get_state()

    assert completed["status"] == "completed"

    assert len(state["pipelines"]) == 1

if __name__ == "__main__":

    test_goal_execution_pipeline()