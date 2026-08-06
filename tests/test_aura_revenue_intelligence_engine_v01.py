from core.business.revenue.aura_revenue_intelligence_engine_v01 import (

    AURARevenueIntelligenceEngine

)

def test_revenue_intelligence_engine():

    engine = AURARevenueIntelligenceEngine()

    opportunity = engine.create_opportunity(

        "AI Company",

        100000,

        80

    )

    forecast = engine.forecast_revenue()

    pipeline = engine.get_revenue_pipeline()

    print(

        "AURA Revenue Intelligence Engine Test"

    )

    print(

        "------------------------------------"

    )

    print(pipeline)

    print(forecast)

    assert opportunity["score"] == (

        "high"

    )

    assert forecast["expected_revenue"] == (

        80000

    )

    assert forecast["opportunities"] == 1

if __name__ == "__main__":

    test_revenue_intelligence_engine()