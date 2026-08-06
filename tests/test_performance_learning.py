from core.learning.performance_learning import (

    PerformanceLearningSystem

)

def test_performance_learning():

    system = PerformanceLearningSystem()

    system.record(

        "React + FastAPI Architecture",

        "success",

        90

    )

    system.record(

        "React + FastAPI Architecture",

        "success",

        95

    )

    result = system.analyze()

    print("Performance Learning Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_performance_learning()