from core.business.aura_revenue_tracking_system_v01 import (

    AURARevenueTrackingSystem

)

def test_revenue_tracking_system():

    system = AURARevenueTrackingSystem()

    deal = system.create_deal(

        "Example Logistics",

        25000,

        "proposal"

    )

    pipeline = system.calculate_pipeline_value()

    updated = system.update_deal_stage(

        deal["id"],

        "negotiation"

    )

    closed = system.close_deal(

        deal["id"]

    )

    print(

        "AURA Revenue Tracking System Test"

    )

    print(

        "---------------------------------"

    )

    print(updated)

    print(

        "Pipeline:",

        pipeline

    )

    print(closed)

    assert pipeline == 25000

    assert updated["stage"] == (

        "negotiation"

    )

    assert closed["status"] == (

        "closed"

    )

if __name__ == "__main__":

    test_revenue_tracking_system()