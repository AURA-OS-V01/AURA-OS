from core.workflow.workflow_manager import WorkflowManager

def test_workflow():

    manager = WorkflowManager()

    workflow = manager.create_workflow(

        "Business Opportunity Analysis",

        [

            "Research Agent",

            "Marketing Agent",

            "Finance Agent",

            "Owner Agent"

        ]

    )

    print("Workflow Manager Test")

    print("--------------------")

    print(workflow)

    updated = manager.next_step(

        workflow["id"]

    )

    print(updated)

if __name__ == "__main__":

    test_workflow()
    