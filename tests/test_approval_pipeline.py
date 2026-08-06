from core.evolution.approval.approval_pipeline import (

    EvolutionApprovalPipeline

)

def test_approval():

    pipeline = EvolutionApprovalPipeline()

    request = pipeline.submit(

        {

            "change":

            "Improve Memory System"

        },

        "medium",

        "passed"

    )

    result = pipeline.approve(

        request["id"]

    )

    print("Evolution Approval Pipeline Test")

    print("--------------------------------")

    print(result)

if __name__ == "__main__":

    test_approval()