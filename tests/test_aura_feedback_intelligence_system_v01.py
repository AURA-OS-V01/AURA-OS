from core.analytics.aura_feedback_intelligence_system_v01 import (

    AURAFeedbackIntelligenceSystem

)

def test_feedback_intelligence():

    system = AURAFeedbackIntelligenceSystem()

    result = system.analyze_feedback(

        "Memory",

        "Improve project context recall",

        10

    )

    print("AURA Feedback Intelligence Test")

    print("--------------------------------")

    print(result)

if __name__ == "__main__":

    test_feedback_intelligence()