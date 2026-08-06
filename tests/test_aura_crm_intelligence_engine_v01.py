from core.business.crm.aura_crm_intelligence_engine_v01 import (

    AURACRMIntelligenceEngine

)

def test_crm_engine():

    crm = AURACRMIntelligenceEngine()

    customer = crm.create_customer(

        "John Smith",

        "Tech Company",

        "john@example.com"

    )

    lead = crm.create_lead(

        "AI Startup",

        "website"

    )

    opportunity = crm.create_opportunity(

        customer["id"],

        10000

    )

    pipeline = crm.get_customer_pipeline()

    print(

        "AURA CRM Intelligence Engine Test"

    )

    print(

        "--------------------------------"

    )

    print(pipeline)

    assert len(

        pipeline["customers"]

    ) == 1

    assert opportunity["status"] == (

        "open"

    )

if __name__ == "__main__":

    test_crm_engine()