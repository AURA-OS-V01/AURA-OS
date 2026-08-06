from core.execution.aura_autonomous_task_execution_loop_v02 import (

    AURAAutonomousTaskExecutionLoop

)

def test_task_execution_loop():

    engine = AURAAutonomousTaskExecutionLoop()

    task = engine.create_goal_task(

        "Create enterprise automation platform",

        "high"

    )

    engine.assign_step(

        task["id"],

        "Design architecture"

    )

    result = engine.execute(

        task["id"]

    )

    state = engine.get_task_state()

    assert result["status"] == "completed"

    assert len(state["tasks"]) == 1

if __name__ == "__main__":

    test_task_execution_loop()