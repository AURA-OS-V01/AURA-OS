from core.integrations.aura_email_connector_v01 import (

    AURAEmailConnector

)

def test_email():

    email = AURAEmailConnector()

    result = email.send_email(

        "business@example.com",

        "AURA Services",

        "We help businesses automate workflows."

    )

    print(result)

if __name__ == "__main__":

    test_email()