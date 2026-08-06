from agents.evolution.research_agent_v01 import (

    AutonomousResearchAgent

)

def test_research_agent():

    agent = AutonomousResearchAgent()

    result = agent.analyze(

        {

            "issue": "Memory retrieval slowdown"

        }

    )

    print("Autonomous Research Agent Test")

    print("------------------------------")

    print(result)

if __name__ == "__main__":

    test_research_agent()