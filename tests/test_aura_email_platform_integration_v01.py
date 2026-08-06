from core.integrations.email.aura_email_platform_integration_v01 import (

    AURAEmailPlatformIntegration

)

def test_email_platform():

    email = AURAEmailPlatformIntegration()

    account = email.connect_account(

        "Gmail",

        "aura@example.com"

    )

    message = email.send_message(

        account["id"],

        "client@example.com",

        "AURA Services",

        "We help businesses automate operations."

    )

    print(

        "AURA Email Platform Integration Test"

    )

    print(account)

    print(message)

    assert account["status"] == "connected"

    assert message["status"] == "sent"

if __name__ == "__main__":

    test_email_platform()