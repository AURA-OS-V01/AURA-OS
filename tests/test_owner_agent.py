from agents.owner.owner_agent import OwnerAgent

def test_owner_agent():

    agent = OwnerAgent()

    agent.add_goal(

        "Help owner manage AURA"

    )

    result = agent.advise(

        "How can AURA scale?"

    )

    print("Owner Agent Test")

    print("----------------")

    print(agent.describe())

    print(result)

if __name__ == "__main__":

    test_owner_agent()