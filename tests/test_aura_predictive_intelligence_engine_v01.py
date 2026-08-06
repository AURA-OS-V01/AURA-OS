from core.intelligence.aura_predictive_intelligence_engine_v01 import (

    AURAPredictiveIntelligenceEngine

)

def test_predictive_engine():

    engine = AURAPredictiveIntelligenceEngine()

    dataset = engine.create_dataset(

        "Monthly Sales"

    )

    engine.add_value(

        dataset["id"],

        100

    )

    engine.add_value(

        dataset["id"],

        150

    )

    prediction = engine.predict_trend(

        dataset["id"]

    )

    print(

        "AURA Predictive Intelligence Engine Test"

    )

    print(

        "----------------------------------------"

    )

    print(prediction)

    assert prediction == (

        "growth"

    )

if __name__ == "__main__":

    test_predictive_engine()