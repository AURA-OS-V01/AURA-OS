from uuid import uuid4

from datetime import datetime

class ErrorAnalysisSystem:

    """

    Analyzes problems and failures.

    """

    def __init__(self):

        self.errors = []

    def record_error(

        self,

        category,

        description,

        severity

    ):

        error = {

            "id": str(uuid4()),

            "category": category,

            "description": description,

            "severity": severity,

            "status": "analyzed",

            "created":

                datetime.utcnow().isoformat()

        }

        self.errors.append(error)

        return error

    def get_errors(

        self,

        severity=None

    ):

        if severity:

            return [

                error

                for error in self.errors

                if error["severity"] == severity

            ]

        return self.errors