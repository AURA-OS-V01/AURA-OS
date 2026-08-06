from core.business.email.aura_email_outreach_engine_v01 import (

    AURAEmailOutreachEngine

)

def test_email_outreach_engine():

    engine = AURAEmailOutreachEngine()

    campaign = engine.create_campaign(

        "AI Startup Outreach",

        "Technology Companies"

    )

    sequence = engine.create_sequence(

        campaign["id"],

        [

            "Introduction email",

            "Follow-up email",

            "Meeting request"

        ]

    )

    launched = engine.launch_campaign(

        campaign["id"]

    )

    response = engine.record_response(

        campaign["id"],

        "interested"

    )

    pipeline = engine.get_outreach_pipeline()

    print(

        "AURA Email Outreach Engine Test"

    )

    print(

        "-------------------------------"

    )

    print(pipeline)

    assert launched["status"] == (

        "active"

    )

    assert sequence["status"] == (

        "ready"

    )

    assert response["type"] == (

        "interested"

    )

if __name__ == "__main__":

    test_email_outreach_engine()