from agents.improvement.improvement_engine import ImprovementEngine

from agents.performance.performance_tracker import PerformanceTracker

from agents.memory.memory_store import MemoryStore

def test_improvement():

    performance = PerformanceTracker()

    performance.record_result(

        "Research Agent",

        True

    )

    performance.record_result(

        "Research Agent",

        True

    )

    memory = MemoryStore(

        "improvement_test.json"

    )

    memory.store(

        "Research Agent",

        {

            "lesson": "Market research succeeded"

        }

    )

    engine = ImprovementEngine(

        performance,

        memory

    )

    result = engine.analyze(

        "Research Agent"

    )

    print("Improvement Engine Test")

    print("-----------------------")

    print(result)

if __name__ == "__main__":

    test_improvement()