class PolicyEngine:

    """

    Evaluates actions against AURA policies.

    """

    def __init__(self, constitution):

        self.constitution = constitution

    def evaluate(

        self,

        action: str,

        context: dict

    ):

        decision = {

            "action": action,

            "allowed": True,

            "reason": "No policy violation detected."

        }

        # Owner vault protection

        if action == "access_owner_vault":

            if context.get("role") != "owner":

                decision["allowed"] = False

                decision["reason"] = (

                    "Only owner can access owner vault."

                )

        return decision