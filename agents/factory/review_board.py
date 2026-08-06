from datetime import datetime

class AgentReviewBoard:

    """

    Reviews new agents before activation.

    """

    def __init__(self):

        self.reviews = []

    def review(

        self,

        blueprint: dict,

        technical_pass: bool,

        security_pass: bool,

        owner_pass: bool

    ):

        approved = (

            technical_pass

            and security_pass

            and owner_pass

        )

        review = {

            "agent": blueprint.get("name"),

            "technical": technical_pass,

            "security": security_pass,

            "owner": owner_pass,

            "approved": approved,

            "reviewed": datetime.utcnow().isoformat()

        }

        self.reviews.append(review)

        return review

    def get_reviews(self):

        return self.reviews