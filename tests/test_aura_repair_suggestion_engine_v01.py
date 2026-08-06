from core.guardian.aura_repair_suggestion_engine_v01 import (

    AURARepairSuggestionEngine

)

def test_repair_suggestion_engine():

    engine = AURARepairSuggestionEngine()

    suggestion = engine.analyze_issue(

        "ImportError",

        "Missing package detected"

    )

    print(

        "AURA Repair Suggestion Engine Test"

    )

    print(

        "----------------------------------"

    )

    print(suggestion)

    assert suggestion["status"] == (

        "generated"

    )

    assert "dependencies" in (

        suggestion["recommendation"]

    )

if __name__ == "__main__":

    test_repair_suggestion_engine()