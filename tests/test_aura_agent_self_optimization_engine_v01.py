from core.agents.optimization.aura_agent_self_optimization_engine_v01 import (

    AURAAgentSelfOptimizationEngine

)

def test_self_optimization_engine():

    engine = AURAAgentSelfOptimizationEngine()

    metric = engine.record_performance(

        "AURA Runtime",

        60,

        "Needs optimization"

    )

    analysis = engine.analyze(

        metric["id"]

    )

    improvement = engine.create_improvement(

        "Runtime",

        "Improve execution speed"

    )

    result = engine.apply_improvement(

        improvement["id"]

    )

    state = engine.get_state()

    assert analysis["recommendation"] == "Optimize performance"

    assert result["status"] == "applied"

    assert len(state["metrics"]) == 1

    assert len(state["improvements"]) == 1

if __name__ == "__main__":

    test_self_optimization_engine()