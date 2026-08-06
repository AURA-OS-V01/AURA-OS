from agents.registry.capability_registry import CapabilityRegistry

from agents.performance.performance_tracker import PerformanceTracker

from agents.selection.adaptive_selector import AdaptiveSelector

def test_selector():

    registry = CapabilityRegistry()

    registry.register_agent(

        "Finance Agent",

        ["financial_analysis"],

        ["read_workspace"]

    )

    registry.register_agent(

        "Analyst Agent",

        ["financial_analysis"],

        ["read_workspace"]

    )

    performance = PerformanceTracker()

    performance.record_result(

        "Finance Agent",

        True

    )

    performance.record_result(

        "Analyst Agent",

        False

    )

    selector = AdaptiveSelector(

        registry,

        performance

    )

    result = selector.select(

        "financial_analysis"

    )

    print("Adaptive Selector Test")

    print("----------------------")

    print(result)

if __name__ == "__main__":

    test_selector()