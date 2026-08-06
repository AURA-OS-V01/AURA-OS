from datetime import datetime

from uuid import uuid4

class DecisionEngine:

    """

    Evaluates options and creates decisions.

    """

    def __init__(self):

        self.name = "AURA Decision Engine"

        self.decisions = []

    def make_decision(

        self,

        objective: str,

        options: list,

        context: dict | None = None

    ):

        decision = {

            "id": str(uuid4()),

            "objective": objective,

            "options": options,

            "selected": options[0] if options else None,

            "reason": "Selected based on available information",

            "confidence": 0.5,

            "context": context or {},

            "created": datetime.utcnow().isoformat()

        }

        self.decisions.append(decision)

        return decision

    def get_decisions(self):

        return self.decisions