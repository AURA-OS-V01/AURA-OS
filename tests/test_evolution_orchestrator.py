from core.evolution.orchestration.evolution_orchestrator import (

    EvolutionOrchestrator

)

def test_orchestrator():

    orchestrator = EvolutionOrchestrator()

    result = orchestrator.create_mission(

        "Improve memory retrieval",

        "Performance Learning System"

    )

    print("Evolution Orchestrator Test")

    print("--------------------------")

    print(result)

if __name__ == "__main__":

    test_orchestrator()