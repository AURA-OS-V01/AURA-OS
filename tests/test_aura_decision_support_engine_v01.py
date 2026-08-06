from core.decision.aura_decision_support_engine_v01 import (

    AURADecisionSupportEngine

)

def test_decision_support_engine():

    engine = AURADecisionSupportEngine()

    decision = engine.create_decision(

        "CRM Platform Selection",

        "Choose best CRM integration provider."

    )

    engine.add_option(

        decision["id"],

        "HubSpot",

        85

    )

    engine.add_option(

        decision["id"],

        "Salesforce",

        95

    )

    recommendation = engine.recommend(

        decision["id"]

    )

    print(

        "AURA Decision Support Engine Test"

    )

    print(

        "---------------------------------"

    )

    print(decision)

    print(recommendation)

    assert recommendation["name"] == (

        "Salesforce"

    )

    assert recommendation["score"] == 95

if __name__ == "__main__":

    test_decision_support_engine()