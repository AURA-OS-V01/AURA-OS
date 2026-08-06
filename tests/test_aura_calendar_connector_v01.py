from core.integrations.aura_calendar_connector_v01 import (

    AURACalendarConnector

)

def test_calendar_connector():

    calendar = AURACalendarConnector()

    result = calendar.create_event(

        "AURA Business Meeting",

        "2026-09-01 10:00",

        [

            "Founder",

            "Client"

        ]

    )

    print("AURA Calendar Connector Test")

    print("----------------------------")

    print(result)

if __name__ == "__main__":

    test_calendar_connector()
