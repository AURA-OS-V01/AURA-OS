from core.learning.improvement_recommendation_system_v01 import (

    ImprovementRecommendationSystem

)

def test_recommendations():

    system = ImprovementRecommendationSystem()

    result = system.create_recommendation(

        "Education Mode",

        "Explanations too complex",

        "Reduce explanation complexity",

        "Medium"

    )

    print("Improvement Recommendation Test")

    print("--------------------------------")

    print(result)

if __name__ == "__main__":

    test_recommendations()