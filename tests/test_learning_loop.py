from agents.learning.learning_loop import LearningLoop

from agents.memory.memory_store import MemoryStore

from agents.performance.performance_tracker import PerformanceTracker

def test_learning():

    memory = MemoryStore(

        "learning_test.json"

    )

    performance = PerformanceTracker()

    loop = LearningLoop(

        memory,

        performance

    )

    result = loop.learn(

        "Research Agent",

        "Market Analysis",

        True,

        "Trend research workflow succeeded"

    )

    print("Learning Loop Test")

    print("------------------")

    print(result)

if __name__ == "__main__":

    test_learning()