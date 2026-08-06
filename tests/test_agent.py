from agents.core.agent import Agent

def test_agent():

    agent = Agent(

        "AURA Assistant",

        "manager"

    )

    agent.add_goal(

        "Help owner manage AURA"

    )

    agent.remember(

        "Owner prefers strategic thinking"

    )

    print("Agent Core Test")

    print("----------------")

    print(agent.describe())

if __name__ == "__main__":

    test_agent()