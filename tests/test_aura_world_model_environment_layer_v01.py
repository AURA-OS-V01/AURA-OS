from core.intelligence.world_model.aura_world_model_environment_layer_v01 import (

    AURAWorldModelEnvironmentLayer

)

def test_world_model_environment_layer():

    world = AURAWorldModelEnvironmentLayer()

    company = world.add_entity(

        "Enterprise AI Market",

        "market",

        "Growing demand for automation solutions"

    )

    signal = world.record_signal(

        "Market Research",

        "trend",

        "AI adoption increasing"

    )

    context = world.update_context(

        "economic_condition",

        "growth"

    )

    state = world.get_world_state()

    print(

        "AURA World Model Environment Layer Test"

    )

    print(

        "--------------------------------------"

    )

    print(state)

    assert len(state["entities"]) == 1

    assert len(state["signals"]) == 1

    assert len(state["context"]) == 1

    assert signal["type"] == "trend"

if __name__ == "__main__":

    test_world_model_environment_layer()