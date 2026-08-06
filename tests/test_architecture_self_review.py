from core.evolution.architecture.self_review import (

    ArchitectureSelfReview

)

def test_architecture_review():

    reviewer = ArchitectureSelfReview()

    result = reviewer.review(

        [

            "agents/runtime",

            "core/execution",

            "core/governance"

        ]

    )

    print("Architecture Self Review Test")

    print("----------------------------")

    print(result)

if __name__ == "__main__":

    test_architecture_review()