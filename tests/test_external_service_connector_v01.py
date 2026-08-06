from tools.connectors.external_service_connector_v01 import (

    ExternalServiceConnector

)

def test_connector():

    connector = ExternalServiceConnector()

    result = connector.register(

        "Database Service"

    )

    print("External Service Connector Test")

    print("--------------------------------")

    print(result)

if __name__ == "__main__":

    test_connector()