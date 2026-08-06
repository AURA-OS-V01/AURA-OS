from core.agents.environment.aura_agent_environment_interaction_engine_v01 import (

    AURAAgentEnvironmentInteractionEngine

)

def test_environment_interaction_engine():

    engine = AURAAgentEnvironmentInteractionEngine()

    environment = engine.create_environment(

        "Business Environment",

        "Customer acquisition workspace"

    )

    engine.update_state(

        environment["id"],

        "customer_count",

        100

    )

    observation = engine.observe(

        "sales_agent",

        environment["id"]

    )

    action = engine.record_action(

        "sales_agent",

        environment["id"],

        "Contact qualified leads"

    )

    print(

        "AURA Agent Environment Interaction Engine Test"

    )

    print(

        "---------------------------------------------"

    )

    print(observation)

    print(action)

    assert observation["state"]["customer_count"] == 100

    assert action["action"] == (

        "Contact qualified leads"

    )

if __name__ == "__main__":

    test_environment_interaction_engine()