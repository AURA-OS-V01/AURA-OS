from core.operations.workflow_automation_engine_v01 import (

    WorkflowAutomationEngine

)

def test_workflow_engine():

    engine = WorkflowAutomationEngine()

    result = engine.create_workflow(

        "Build client dashboard"

    )

    print("Workflow Automation Engine Test")

    print("--------------------------------")

    print(result)

if __name__ == "__main__":

    test_workflow_engine()