from core.analytics.aura_testing_analytics_engine_v01 import (

    AURATestingAnalyticsEngine

)

def test_testing_analytics():

    system = AURATestingAnalyticsEngine()

    result = system.record_metric(

        "Test User",

        "task_success_rate",

        95

    )

    print("AURA Testing Analytics Test")

    print("--------------------------")

    print(result)

if __name__ == "__main__":

    test_testing_analytics()