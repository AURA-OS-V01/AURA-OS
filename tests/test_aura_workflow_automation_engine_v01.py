from core.workflows.aura_workflow_automation_engine_v01 import (

    AURAWorkflowAutomationEngine

)

def test_workflow_automation_engine():

    engine = AURAWorkflowAutomationEngine()

    workflow = engine.create_workflow(

        "Client Acquisition Workflow",

        [

            "Find Lead",

            "Score Lead",

            "Create Sales Strategy",

            "Send Outreach",

            "Schedule Follow-up"

        ]

    )

    started = engine.start_workflow(

        workflow["id"]

    )

    completed_step = engine.complete_step(

        workflow["id"],

        1

    )

    print(

        "AURA Workflow Automation Engine Test"

    )

    print(

        "------------------------------------"

    )

    print(started)

    print(completed_step)

    assert started["status"] == (

        "running"

    )

    assert completed_step["status"] == (

        "completed"

    )

if __name__ == "__main__":

    test_workflow_automation_engine()