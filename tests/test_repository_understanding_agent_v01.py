from agents.engineering.repository_understanding_agent_v01 import (

    RepositoryUnderstandingAgent

)

def test_repository_agent():

    agent = RepositoryUnderstandingAgent()

    result = agent.analyze(

        "AURA Repository"

    )

    print("Repository Understanding Agent Test")

    print("----------------------------------")

    print(result)

if __name__ == "__main__":

    test_repository_agent()