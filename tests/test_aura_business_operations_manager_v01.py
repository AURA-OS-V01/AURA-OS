from core.business.aura_business_operations_manager_v01 import (

    AURABusinessOperationsManager

)

def test_business_operations_manager():

    system = AURABusinessOperationsManager()

    agent = system.register_agent(

        "Sales Agent",

        "growth"

    )

    task = system.create_task(

        "Contact qualified logistics companies",

        agent["name"]

    )

    updated = system.update_task_status(

        task["id"],

        "completed"

    )

    print(

        "AURA Business Operations Manager Test"

    )

    print(

        "------------------------------------"

    )

    print(agent)

    print(updated)

    assert agent["status"] == "available"

    assert updated["status"] == "completed"

if __name__ == "__main__":

    test_business_operations_manager()