from agents.performance.performance_tracker import PerformanceTracker

def test_performance():

    tracker = PerformanceTracker()

    tracker.register_agent(

        "Finance Agent"

    )

    tracker.record_result(

        "Finance Agent",

        True

    )

    tracker.record_result(

        "Finance Agent",

        True

    )

    tracker.record_result(

        "Finance Agent",

        False

    )

    print("Performance Tracker Test")

    print("------------------------")

    print(

        tracker.get_score(

            "Finance Agent"

        )

    )

if __name__ == "__main__":

    test_performance()