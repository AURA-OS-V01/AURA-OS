class AgentTester:

    """

    Tests proposed AURA agents

    before approval.

    """

    def __init__(self):

        self.results = []

    def test_blueprint(

        self,

        blueprint: dict

    ):

        result = {

            "agent": blueprint.get("name"),

            "passed": True,

            "checks": []

        }

        required = [

            "name",

            "role",

            "purpose"

        ]

        for field in required:

            if field in blueprint:

                result["checks"].append(

                    f"{field}: OK"

                )

            else:

                result["passed"] = False

                result["checks"].append(

                    f"{field}: MISSING"

                )

        self.results.append(result)

        return result

    def get_results(self):

        return self.results