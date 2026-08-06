from core.agents.aura_task_delegation_engine_v01 import (

    AURATaskDelegationEngine

)

def test_task_delegation_engine():

    engine = AURATaskDelegationEngine()

    engine.register_agent(

        "Lead Intelligence Agent",

        [

            "lead_generation",

            "research"

        ]

    )

    engine.register_agent(

        "Sales Agent",

        [

            "sales_strategy"

        ]

    )

    result = engine.delegate_task(

        "Find AI automation prospects",

        "lead_generation"

    )

    print(

        "AURA Task Delegation Engine Test"

    )

    print(

        "--------------------------------"

    )

    print(result)

    assert result["assigned_agent"] == (

        "Lead Intelligence Agent"

    )

    assert result["status"] == (

        "assigned"

    )

if __name__ == "__main__":

    test_task_delegation_engine()