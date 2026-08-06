from core.growth.opportunity_intelligence_v01 import (

    AURAOpportunityIntelligence

)

def test_opportunity_intelligence():

    system = AURAOpportunityIntelligence()

    lead = {

        "company":

            "Example Logistics",

        "score":

            95

    }

    result = system.analyze_opportunity(

        lead

    )

    print("AURA Opportunity Intelligence Test")

    print("----------------------------------")

    print(result)

if __name__ == "__main__":

    test_opportunity_intelligence()