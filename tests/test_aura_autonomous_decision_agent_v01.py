from core.agents.autonomy.aura_autonomous_decision_agent_v01 import (

    AURAAutonomousDecisionAgent

)

def test_autonomous_decision_agent():

    agent = AURAAutonomousDecisionAgent()

    decision = agent.analyze_options(

        "Choose customer acquisition strategy",

        [

            {

                "action":

                    "AI Outreach Campaign",

                "score":

                    90

            },

            {

                "action":

                    "Manual Cold Calling",

                "score":

                    60

            }

        ]

    )

    result = agent.choose_action(

        decision["id"]

    )

    print(

        "AURA Autonomous Decision Agent Test"

    )

    print(

        "------------------------------------"

    )

    print(result)

    assert result["selected"] == (

        "AI Outreach Campaign"

    )

    assert result["confidence"] == 90

if __name__ == "__main__":

    test_autonomous_decision_agent()