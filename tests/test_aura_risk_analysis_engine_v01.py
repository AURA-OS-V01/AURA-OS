from core.intelligence.aura_risk_analysis_engine_v01 import (

    AURARiskAnalysisEngine

)

def test_risk_analysis_engine():

    engine = AURARiskAnalysisEngine()

    risk = engine.add_risk(

        "Customer Data Exposure",

        "security",

        9

    )

    level = engine.analyze_risk_level(

        risk["id"]

    )

    print(

        "AURA Risk Analysis Engine Test"

    )

    print(

        "--------------------------------"

    )

    print(risk)

    print(level)

    assert level == "critical"

if __name__ == "__main__":

    test_risk_analysis_engine()