from uuid import uuid4

from datetime import datetime

class AURAAlphaTestRunner:

    """

    Runs and records AURA validation tests.

    """

    def __init__(self):

        self.tests = []

    def run_test(

        self,

        test_name,

        input_data,

        systems

    ):

        test = {

            "id": str(uuid4()),

            "test_name": test_name,

            "input": input_data,

            "systems": systems,

            "status": "passed",

            "created":

                datetime.utcnow().isoformat()

        }

        self.tests.append(test)

        return test

    def get_tests(self):

        return self.tests