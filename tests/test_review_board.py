from agents.factory.generator import AgentGenerator

from agents.factory.review_board import AgentReviewBoard

def test_review_board():

    generator = AgentGenerator()

    blueprint = generator.create_blueprint(

        "AURA Legal Agent",

        "legal_specialist",

        "Compliance assistance"

    )

    board = AgentReviewBoard()

    result = board.review(

        blueprint,

        True,

        True,

        True

    )

    print("Agent Review Board Test")

    print("----------------------")

    print(result)

if __name__ == "__main__":

    test_review_board()