class RiskClassifier:

    """

    Evaluates mission risk.

    """

    def __init__(self):

        self.rules = {

            "read": "low",

            "research": "low",

            "financial": "medium",

            "code_execution": "high",

            "system_change": "critical"

        }

    def classify(

        self,

        actions: list

    ):

        levels = []

        for action in actions:

            if action in self.rules:

                levels.append(

                    self.rules[action]

                )

        if "critical" in levels:

            return "critical"

        if "high" in levels:

            return "high"

        if "medium" in levels:

            return "medium"

        return "low"