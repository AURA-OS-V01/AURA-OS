from core.testing.research_mode_validation_v01 import (

    ResearchModeValidation

)

def test_research_mode():

    system = ResearchModeValidation()

    result = system.run_validation(

        "Test User",

        "Research renewable energy trends",

        [

            "Knowledge Retrieval",

            "Organization",

            "Summarization",

            "Source Tracking"

        ]

    )

    print("Research Mode Validation")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_research_mode()