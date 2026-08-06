from core.decision.aura_recommendation_engine_v01 import (

    AURARecommendationEngine

)

def test_recommendation_engine():

    engine = AURARecommendationEngine()

    recommendation = engine.create_recommendation(

        "business_owner",

        "Need customer automation solution"

    )

    engine.add_option(

        recommendation["id"],

        "AI Sales Agent",

        90

    )

    engine.add_option(

        recommendation["id"],

        "Manual Sales Team",

        60

    )

    result = engine.generate(

        recommendation["id"]

    )

    print(

        "AURA Recommendation Engine Test"

    )

    print(

        "--------------------------------"

    )

    print(result)

    assert result["option"] == (

        "AI Sales Agent"

    )

    assert result["priority"] == 90

if __name__ == "__main__":

    test_recommendation_engine()