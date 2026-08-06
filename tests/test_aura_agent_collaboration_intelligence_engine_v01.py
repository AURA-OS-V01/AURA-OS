from core.agents.collaboration.aura_agent_collaboration_intelligence_engine_v01 import (

    AURAAgentCollaborationIntelligenceEngine

)

def test_collaboration_intelligence_engine():

    engine = AURAAgentCollaborationIntelligenceEngine()

    engine.record_collaboration(

        [

            "sales_agent",

            "research_agent"

        ],

        "Find new customers",

        True,

        90

    )

    report = engine.analyze_team(

        [

            "sales_agent",

            "research_agent"

        ]

    )

    suggestion = engine.suggest_team_improvement(

        [

            "sales_agent",

            "research_agent"

        ]

    )

    print(

        "AURA Agent Collaboration Intelligence Engine Test"

    )

    print(

        "-----------------------------------------------"

    )

    print(report)

    print(suggestion)

    assert report["average_score"] == 90

    assert suggestion == (

        "Team performance is optimal"

    )

if __name__ == "__main__":

    test_collaboration_intelligence_engine()