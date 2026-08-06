from core.agents.workflows.aura_agent_workflow_engine_v01 import (

    AURAAgentWorkflowEngine

)

def test_agent_workflow_engine():

    engine = AURAAgentWorkflowEngine()

    workflow = engine.create_workflow(

        "Customer Acquisition Pipeline",

        "Automated lead discovery workflow"

    )

    engine.add_step(

        workflow["id"],

        "Research Customers",

        "research_agent"

    )

    engine.add_step(

        workflow["id"],

        "Contact Leads",

        "sales_agent"

    )

    result = engine.execute_workflow(

        workflow["id"]

    )

    print(

        "AURA Agent Workflow Engine Test"

    )

    print(

        "--------------------------------"

    )

    print(result)

    assert result["status"] == (

        "completed"

    )

    assert len(result["steps"]) == 2

if __name__ == "__main__":

    test_agent_workflow_engine()