from core.business.marketing.aura_marketing_automation_engine_v01 import (

    AURAMarketingAutomationEngine

)

def test_marketing_automation_engine():

    engine = AURAMarketingAutomationEngine()

    audience = engine.create_audience(

        "Software Companies",

        "AI and technology businesses"

    )

    campaign = engine.create_campaign(

        audience["id"],

        "AI Growth Campaign",

        "Generate qualified leads"

    )

    task = engine.create_marketing_task(

        campaign["id"],

        "Create email campaign"

    )

    launched = engine.launch_campaign(

        campaign["id"]

    )

    pipeline = engine.get_marketing_pipeline()

    print(

        "AURA Marketing Automation Engine Test"

    )

    print(

        "------------------------------------"

    )

    print(pipeline)

    assert launched["status"] == (

        "active"

    )

    assert task["status"] == (

        "pending"

    )

if __name__ == "__main__":

    test_marketing_automation_engine()