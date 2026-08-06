from core.agents.knowledge.aura_agent_knowledge_integration_engine_v01 import (

    AURAAgentKnowledgeIntegrationEngine

)

def test_agent_knowledge_integration_engine():

    engine = AURAAgentKnowledgeIntegrationEngine()

    engine.add_knowledge(

        "AI Sales Automation",

        "AI agents can automate customer outreach.",

        "knowledge_repository"

    )

    context = engine.get_agent_context(

        "sales_agent",

        "AI Sales"

    )

    print(

        "AURA Agent Knowledge Integration Engine Test"

    )

    print(

        "-------------------------------------------"

    )

    print(context)

    assert context["agent_id"] == (

        "sales_agent"

    )

    assert len(context["context"]) == 1

if __name__ == "__main__":

    test_agent_knowledge_integration_engine()