from core.integrations.payment.aura_payment_integration_v01 import (

    AURAPaymentIntegration

)

def test_payment_integration():

    payment = AURAPaymentIntegration()

    provider = payment.connect_provider(

        "Stripe",

        "aura_business_account"

    )

    transaction = payment.create_transaction(

        provider["id"],

        "Example Logistics",

        5000,

        "USD"

    )

    updated = payment.update_transaction_status(

        transaction["id"],

        "completed"

    )

    print(

        "AURA Payment Integration Test"

    )

    print(provider)

    print(updated)

    assert provider["status"] == "connected"

    assert updated["status"] == "completed"

if __name__ == "__main__":

    test_payment_integration()