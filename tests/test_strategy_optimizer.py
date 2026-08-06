from core.learning.strategy_optimizer import (

    StrategyOptimizer

)

def test_strategy_optimizer():

    optimizer = StrategyOptimizer()

    optimizer.evaluate(

        [

            "Plan",

            "Prototype",

            "Test"

        ],

        95

    )

    optimizer.evaluate(

        [

            "Build",

            "Fix Bugs"

        ],

        60

    )

    result = optimizer.recommend()

    print("Strategy Optimizer Test")

    print("-----------------------")

    print(result)

if __name__ == "__main__":

    test_strategy_optimizer()