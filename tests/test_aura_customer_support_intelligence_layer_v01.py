from core.business.support.aura_customer_support_intelligence_layer_v01 import (

    AURACustomerSupportIntelligenceLayer

)

def test_customer_support_layer():

    support = AURACustomerSupportIntelligenceLayer()

    ticket = support.create_ticket(

        "Customer A",

        "Software login problem",

        "high"

    )

    analysis = support.analyze_ticket(

        ticket["id"]

    )

    response = support.create_response_task(

        ticket["id"],

        "Reset account access"

    )

    resolved = support.resolve_ticket(

        ticket["id"]

    )

    pipeline = support.get_support_pipeline()

    print(

        "AURA Customer Support Intelligence Layer Test"

    )

    print(

        "---------------------------------------------"

    )

    print(pipeline)

    assert analysis["priority"] == (

        "urgent"

    )

    assert resolved["status"] == (

        "resolved"

    )

    assert response["status"] == (

        "pending"

    )

if __name__ == "__main__":

    test_customer_support_layer()