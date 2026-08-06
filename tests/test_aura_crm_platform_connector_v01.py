from core.integrations.crm.aura_crm_platform_connector_v01 import (

    AURACRMPlatformConnector

)

def test_crm_connector():

    crm = AURACRMPlatformConnector()

    connection = crm.connect_provider(

        "HubSpot",

        "aura_account"

    )

    contact = crm.sync_contact(

        connection["id"],

        "John Smith",

        "Example Logistics",

        "john@example.com"

    )

    print(

        "AURA CRM Platform Connector Test"

    )

    print(connection)

    print(contact)

    assert connection["status"] == "connected"

    assert contact["status"] == "synced"

if __name__ == "__main__":

    test_crm_connector()