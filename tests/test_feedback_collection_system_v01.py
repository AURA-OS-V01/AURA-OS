from core.learning.feedback_collection_system_v01 import (

    FeedbackCollectionSystem

)

def test_feedback_collection():

    system = FeedbackCollectionSystem()

    result = system.record_feedback(

        "User",

        "Education",

        "Explanation was too advanced",

        3

    )

    print("Feedback Collection Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_feedback_collection()