from core.growth.outreach_agent_v01 import (

    AURAOutreachAgent

)

def test_outreach_agent():

    agent = AURAOutreachAgent()

    lead = {

        "company":

            "Example Logistics",

        "industry":

            "Transportation",

        "contact":

            "CEO"

    }

    result = agent.create_outreach(

        lead,

        "Personalized automation offer"

    )

    print("AURA Outreach Agent Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_outreach_agent()