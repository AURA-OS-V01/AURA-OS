from core.agents.simulation.aura_agent_simulation_testing_environment_v01 import (

    AURAAgentSimulationTestingEnvironment

)

def test_simulation_testing_environment():

    environment = AURAAgentSimulationTestingEnvironment()

    scenario = environment.create_scenario(

        "Sales Strategy Simulation",

        "Test customer acquisition behavior"

    )

    environment.run_simulation(

        "sales_agent",

        scenario["id"],

        95

    )

    evaluation = environment.evaluate_agent(

        "sales_agent"

    )

    print(

        "AURA Agent Simulation Testing Environment Test"

    )

    print(

        "---------------------------------------------"

    )

    print(evaluation)

    assert evaluation["average_score"] == 95

    assert evaluation["tests"] == 1

if __name__ == "__main__":

    test_simulation_testing_environment()