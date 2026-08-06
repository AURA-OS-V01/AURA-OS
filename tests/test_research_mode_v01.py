from aura_platform.research.research_mode_v01 import (

    ResearchMode

)

def test_research_mode():

    research = ResearchMode()

    result = research.create_project(

        "AI Education Trends",

        "Market Research"

    )

    print("Research Mode Test")

    print("------------------")

    print(result)

if __name__ == "__main__":

    test_research_mode()