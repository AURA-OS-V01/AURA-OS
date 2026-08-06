from agents.development.developer_agent import DeveloperAgent

def test_developer_agent():

    agent = DeveloperAgent()

    result = agent.create_task(

        "Improve AURA dashboard"

    )

    print("Developer Agent Test")

    print("-------------------")

    print(agent.describe())

    print(result)

if __name__ == "__main__":

    test_developer_agent()