from core.intelligence.strategy.aura_strategy_optimization_engine_v01 import (

    AURAStrategyOptimizationEngine

)

def test_strategy_optimization_engine():

    engine = AURAStrategyOptimizationEngine()

    strategy_one = engine.create_strategy(

        "Enterprise Expansion",

        "Increase enterprise customers",

        90

    )

    strategy_two = engine.create_strategy(

        "Small Business Expansion",

        "Increase SMB customers",

        70

    )

    evaluation_one = engine.evaluate_strategy(

        strategy_one["id"],

        10

    )

    evaluation_two = engine.evaluate_strategy(

        strategy_two["id"],

        20

    )

    recommendation = engine.recommend_strategy()

    state = engine.get_strategy_state()

    print(

        "AURA Strategy Optimization Engine Test"

    )

    print(

        "--------------------------------------"

    )

    print(state)

    assert evaluation_one["score"] == 80

    assert evaluation_two["score"] == 50

    assert recommendation["strategy_id"] == (

        strategy_one["id"]

    )

if __name__ == "__main__":

    test_strategy_optimization_engine()