from core.integrations.aura_business_connector_v01 import (

    AURABusinessConnector

)

def test_business_connector():

    business = AURABusinessConnector()

    result = business.connect_business_tool(

        "Sales CRM",

        "customer_management"

    )

    print("AURA Business Connector Test")

    print("----------------------------")

    print(result)

if __name__ == "__main__":

    test_business_connector()