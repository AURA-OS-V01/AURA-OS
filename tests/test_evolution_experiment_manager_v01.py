from core.evolution.evolution_experiment_manager_v01 import (

    EvolutionExperimentManager

)

def test_experiment_manager():

    manager = EvolutionExperimentManager()

    experiment = manager.create_experiment(

        "Improve memory retrieval",

        "Add indexing"

    )

    result = manager.complete(

        experiment["id"],

        True

    )

    print("Evolution Experiment Manager Test")

    print("---------------------------------")

    print(result)

if __name__ == "__main__":

    test_experiment_manager()