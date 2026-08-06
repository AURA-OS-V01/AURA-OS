from agents.engineering.code_review_agent_v01 import (

    CodeReviewAgent

)

def test_code_review_agent():

    agent = CodeReviewAgent()

    result = agent.review(

        "Add AURA dashboard"

    )

    print("Code Review Agent Test")

    print("---------------------")

    print(result)

if __name__ == "__main__":

    test_code_review_agent()