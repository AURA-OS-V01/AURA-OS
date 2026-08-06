from core.knowledge.aura_semantic_search_engine_v01 import (

    AURASemanticSearchEngine

)

def test_semantic_search():

    engine = AURASemanticSearchEngine()

    document = {

        "id": "doc1",

        "title": "Automation",

        "content": "AI agents build enterprise workflows.",

        "category": "technology"

    }

    engine.index_document(

        document

    )

    results = engine.search(

        "enterprise"

    )

    assert len(results) == 1

    assert results[0]["document_id"] == "doc1"

if __name__ == "__main__":

    test_semantic_search()