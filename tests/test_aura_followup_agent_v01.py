from core.growth.followup_agent_v01 import (

    AURAFollowupAgent

)

def test_followup_agent():

    agent = AURAFollowupAgent()

    result = agent.create_followup(

        "Example Logistics",

        "CEO",

        3

    )

    print("AURA Follow-up Agent Test")

    print("-------------------------")

    print(result)

if __name__ == "__main__":

    test_followup_agent()