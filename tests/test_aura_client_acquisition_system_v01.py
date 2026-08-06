from core.business.acquisition.aura_client_acquisition_system_v01 import (

    AURAClientAcquisitionSystem

)

def test_client_acquisition_system():

    system = AURAClientAcquisitionSystem()

    prospect = system.add_prospect(

        "AI Software Company",

        "technology",

        90

    )

    qualified = system.qualify_prospect(

        prospect["id"]

    )

    campaign = system.create_acquisition_campaign(

        "Technology Growth Campaign",

        "AI Companies"

    )

    conversion = system.record_conversion(

        prospect["id"],

        25000

    )

    pipeline = system.get_acquisition_pipeline()

    print(

        "AURA Client Acquisition System Test"

    )

    print(

        "-----------------------------------"

    )

    print(pipeline)

    assert qualified["status"] == (

        "qualified"

    )

    assert campaign["status"] == (

        "active"

    )

    assert conversion["status"] == (

        "converted"

    )

if __name__ == "__main__":

    test_client_acquisition_system()