from uuid import uuid4

from datetime import datetime

class SafetyPolicyFramework:

    """

    Defines and checks AURA safety policies.

    """

    def __init__(self):

        self.policies = []

    def add_policy(

        self,

        action,

        rule,

        status

    ):

        policy = {

            "id": str(uuid4()),

            "action": action,

            "rule": rule,

            "status": status,

            "created":

                datetime.utcnow().isoformat()

        }

        self.policies.append(policy)

        return policy

    def check_action(

        self,

        action

    ):

        for policy in self.policies:

            if policy["action"] == action:

                return policy["status"]

        return "review_required"