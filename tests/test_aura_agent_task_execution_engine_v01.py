from core.agents.aura_agent_task_execution_engine_v01 import (

    AURAAgentTaskExecutionEngine

)

def test_agent_task_execution_engine():

    engine = AURAAgentTaskExecutionEngine()

    task = engine.create_task(

        "agent_sales_001",

        "Analyze potential customer leads"

    )

    execution = engine.execute_task(

        task["id"]

    )

    history = engine.get_history()

    print(

        "AURA Agent Task Execution Engine Test"

    )

    print(

        "-------------------------------------"

    )

    print(task)

    print(execution)

    print(history)

    assert execution["status"] == (

        "completed"

    )

    assert len(history) == 1

if __name__ == "__main__":

    test_agent_task_execution_engine()