from uuid import uuid4

from datetime import datetime

class AURATestFailureAnalyzer:

    def __init__(self):

        self.failures = []

        self.results = []

    def record_test_result(

        self,

        test_name,

        status

    ):

        result = {

            "id":

                str(uuid4()),

            "test":

                test_name,

            "status":

                status,

            "created":

                datetime.utcnow().isoformat()

        }

        self.results.append(result)

        return result

    def record_failure(

        self,

        test_name,

        error_type,

        message

    ):

        failure = {

            "id":

                str(uuid4()),

            "test":

                test_name,

            "error_type":

                error_type,

            "message":

                message,

            "category":

                self.categorize_error(

                    error_type

                ),

            "created":

                datetime.utcnow().isoformat()

        }

        self.failures.append(failure)

        return failure

    def categorize_error(

        self,

        error_type

    ):

        categories = {

            "ImportError":

                "dependency",

            "SyntaxError":

                "code_structure",

            "AssertionError":

                "logic",

            "TypeError":

                "data_handling"

        }

        return categories.get(

            error_type,

            "unknown"

        )

    def generate_report(self):

        return {

            "total_tests":

                len(self.results),

            "total_failures":

                len(self.failures),

            "failures":

                self.failures

        }