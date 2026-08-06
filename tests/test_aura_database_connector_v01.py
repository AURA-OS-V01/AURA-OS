from core.integrations.aura_database_connector_v01 import (

    AURADatabaseConnector

)

def test_database_connector():

    database = AURADatabaseConnector()

    database.insert(

        "users",

        {

            "name": "Test User",

            "plan": "Alpha"

        }

    )

    result = database.query(

        "users"

    )

    print("AURA Database Connector Test")

    print("----------------------------")

    print(result)

if __name__ == "__main__":

    test_database_connector()