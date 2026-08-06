from core.agents.learning.aura_agent_learning_engine_v01 import (

    AURAAgentLearningEngine

)

def test_agent_learning_engine():

    engine = AURAAgentLearningEngine()

    experience = engine.record_experience(

        "sales_agent",

        "Customer analysis",

        "successful",

        95

    )

    evaluation = engine.evaluate_agent(

        "sales_agent"

    )

    print(

        "AURA Agent Learning Engine Test"

    )

    print(

        "--------------------------------"

    )

    print(experience)

    print(evaluation)

    assert experience["outcome"] == (

        "successful"

    )

    assert evaluation["average_score"] == 95

if __name__ == "__main__":

    test_agent_learning_engine()