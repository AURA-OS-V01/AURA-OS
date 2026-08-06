class AuraConstitution:

    """

    Core principles that govern AURA behavior.

    """

    def __init__(self):

        self.rules = [

            {

                "id": "OWNER_PRIVACY",

                "rule": "Protect owner information and private data."

            },

            {

                "id": "WORKSPACE_ISOLATION",

                "rule": "Never allow unauthorized workspace data access."

            },

            {

                "id": "APPROVAL_REQUIRED",

                "rule": "High-risk actions require authorization."

            },

            {

                "id": "EXPLAINABILITY",

                "rule": "Important decisions must be explainable."

            }

        ]

    def get_rules(self):

        return self.rules