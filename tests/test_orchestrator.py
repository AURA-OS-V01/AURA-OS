from core.orchestrator.aura_orchestrator import AURAOrchestrator

def test_orchestrator():

    aura = AURAOrchestrator()

    aura.register_agent(

        "Developer Agent",

        "developer"

    )

    task = aura.create_task(

        "Build new AURA feature"

    )

    result = aura.assign_task(

        task["id"],

        "Developer Agent"

    )

    print("AURA Orchestrator Test")

    print("---------------------")

    print(result)

if __name__ == "__main__":

    test_orchestrator()