from core.integrations.aura_api_connector_v01 import (

    AURAAPIConnector

)

def test_api_connector():

    api = AURAAPIConnector()

    result = api.add_api(

        "CRM Platform",

        "https://example-crm.com/api"

    )

    print("AURA API Connector Test")

    print("-----------------------")

    print(result)

if __name__ == "__main__":

    test_api_connector()