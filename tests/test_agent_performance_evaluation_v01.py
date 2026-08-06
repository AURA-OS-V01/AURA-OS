from core.agents.agent_performance_evaluation_v01 import (

    AgentPerformanceEvaluation

)

def test_agent_performance():

    system = AgentPerformanceEvaluation()

    result = system.record_performance(

        "Backend Agent",

        120,

        "96%"

    )

    print("Agent Performance Evaluation Test")

    print("---------------------------------")

    print(result)

if __name__ == "__main__":

    test_agent_performance()