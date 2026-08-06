from core.learning.architecture_recommendation import (

    ArchitectureRecommendationEngine

)

def test_architecture_recommendation():

    engine = ArchitectureRecommendationEngine()

    result = engine.recommend(

        "AI Dashboard",

        [

            "React + FastAPI",

            "React + FastAPI",

            "React + FastAPI"

        ]

    )

    print("Architecture Recommendation Test")

    print("--------------------------------")

    print(result)

if __name__ == "__main__":

    test_architecture_recommendation()