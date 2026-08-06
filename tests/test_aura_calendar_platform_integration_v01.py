from core.integrations.calendar.aura_calendar_platform_integration_v01 import (

    AURACalendarPlatformIntegration

)

def test_calendar_platform():

    calendar = AURACalendarPlatformIntegration()

    account = calendar.connect_calendar(

        "Google Calendar",

        "aura@example.com"

    )

    event = calendar.create_event(

        account["id"],

        "Client Discovery Meeting",

        "2026-09-01 10:00",

        [

            "AURA",

            "Client"

        ]

    )

    print(

        "AURA Calendar Platform Integration Test"

    )

    print(account)

    print(event)

    assert account["status"] == "connected"

    assert event["status"] == "scheduled"

if __name__ == "__main__":

    test_calendar_platform()