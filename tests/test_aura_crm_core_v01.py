from core.crm.aura_crm_core_v01 import (

    AURACRMCore

)

def test_crm_core():

    crm = AURACRMCore()

    client = crm.create_client(

        "Example Logistics",

        "Transportation",

        "CEO"

    )

    interaction = crm.add_interaction(

        client["id"],

        "meeting",

        "Discussed AI automation implementation."

    )

    history = crm.get_client_history(

        client["id"]

    )

    print(

        "AURA CRM Core Test"

    )

    print(

        "------------------"

    )

    print(client)

    print(interaction)

    print(history)

    assert client["status"] == (

        "active"

    )

    assert history[0]["type"] == (

        "meeting"

    )

if __name__ == "__main__":

    test_crm_core()