from core.knowledge.aura_knowledge_repository_v01 import (

    AURAKnowledgeRepository

)

def test_knowledge_repository():

    repo = AURAKnowledgeRepository()

    doc = repo.add_knowledge(

        "AI Automation",

        "Enterprise automation systems use intelligent agents.",

        "technology"

    )

    results = repo.search(

        "intelligent agents"

    )

    state = repo.get_state()

    assert doc["category"] == "technology"

    assert len(results) == 1

    assert len(state["documents"]) == 1

if __name__ == "__main__":

    test_knowledge_repository()