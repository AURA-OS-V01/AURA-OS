from core.business.workflows.aura_workflow_automation_builder_v01 import (

    AURAWorkflowAutomationBuilder

)

def test_workflow_automation_builder():

    builder = AURAWorkflowAutomationBuilder()

    workflow = builder.create_workflow(

        "Lead Follow Up",

        "new_lead_created"

    )

    builder.add_step(

        workflow["id"],

        "Send introduction email"

    )

    builder.add_step(

        workflow["id"],

        "Create sales task"

    )

    activated = builder.activate_workflow(

        workflow["id"]

    )

    execution = builder.execute_workflow(

        workflow["id"],

        "New qualified lead"

    )

    data = builder.get_workflows()

    print(

        "AURA Workflow Automation Builder Test"

    )

    print(

        "------------------------------------"

    )

    print(data)

    assert activated["status"] == (

        "active"

    )

    assert execution["status"] == (

        "completed"

    )

    assert len(

        workflow["steps"]

    ) == 2

if __name__ == "__main__":

    test_workflow_automation_builder()