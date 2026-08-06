from core.business.sales.aura_sales_automation_agent_v01 import (

    AURASalesAutomationAgent

)

def test_sales_agent():

    agent = AURASalesAutomationAgent()

    lead = agent.evaluate_lead(

        "AI Startup",

        "AI",

        100000

    )

    action = agent.create_sales_action(

        lead["id"],

        "Prepare outreach campaign"

    )

    pipeline = agent.get_pipeline()

    print(

        "AURA Sales Automation Agent Test"

    )

    print(

        "--------------------------------"

    )

    print(pipeline)

    assert lead["status"] == (

        "high_priority"

    )

    assert action["status"] == (

        "created"

    )

if __name__ == "__main__":

    test_sales_agent()
    