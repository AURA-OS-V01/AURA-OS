from uuid import uuid4

class PatternRecognitionEngine:

    """

    Finds reusable patterns

    from engineering history.

    """

    def __init__(self):

        self.patterns = []

    def analyze(

        self,

        memories

    ):

        successful = []

        for memory in memories:

            if memory.get(

                "outcome"

            ) == "success":

                successful.append(

                    memory["decision"]

                )

        pattern = {

            "id": str(uuid4()),

            "successful_decisions":

                successful,

            "count":

                len(successful)

        }

        self.patterns.append(

            pattern

        )

        return pattern

    def get_patterns(self):

        return self.patterns