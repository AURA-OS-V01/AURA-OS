from core.knowledge.documents.aura_document_intelligence_engine_v01 import (

    AURADocumentIntelligenceEngine

)

def test_document_engine():

    engine = AURADocumentIntelligenceEngine()

    document = engine.ingest_document(

        "Sales Strategy.pdf",

        "pdf",

        "AURA helps businesses automate operations."

    )

    text = engine.extract_text(

        document["id"]

    )

    print(

        "AURA Document Intelligence Engine Test"

    )

    print(

        "--------------------------------------"

    )

    print(document)

    print(text)

    assert document["status"] == "processed"

    assert text == (

        "AURA helps businesses automate operations."

    )

if __name__ == "__main__":

    test_document_engine()