from core.growth.lead_intelligence_engine_v01 import (

    AURALeadIntelligenceEngine

)

def test_lead_intelligence():

    system = AURALeadIntelligenceEngine()

    lead = system.create_lead(

        "Example Logistics",

        "Transportation",

        "CEO"

    )

    result = system.score_lead(

        lead["id"],

        90

    )

    print("AURA Lead Intelligence Engine Test")

    print("----------------------------------")

    print(result)

if __name__ == "__main__":

    test_lead_intelligence()
    