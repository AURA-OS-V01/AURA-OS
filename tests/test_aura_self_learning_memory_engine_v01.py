from core.intelligence.memory.aura_self_learning_memory_engine_v01 import (

    AURASelfLearningMemoryEngine

)

def test_self_learning_memory_engine():

    memory = AURASelfLearningMemoryEngine()

    experience = memory.record_experience(

        "Launch customer outreach workflow",

        "High-value technology prospect"

    )

    outcome = memory.record_outcome(

        experience["id"],

        "Successful conversion"

    )

    pattern = memory.learn_pattern(

        "Personalized outreach improves conversion",

        "Increase personalization priority"

    )

    state = memory.get_memory_state()

    print(

        "AURA Self Learning Memory Engine Test"

    )

    print(

        "------------------------------------"

    )

    print(state)

    assert outcome["outcome"] == (

        "Successful conversion"

    )

    assert pattern["improvement"] == (

        "Increase personalization priority"

    )

    assert len(

        state["experiences"]

    ) == 1

if __name__ == "__main__":

    test_self_learning_memory_engine()