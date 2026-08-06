from uuid import uuid4

from datetime import datetime

class AURASelfTestOrchestrator:

    def __init__(self):

        self.test_runs = []

        self.failures = []

    def start_test_cycle(

        self,

        name

    ):

        cycle = {

            "id":

                str(uuid4()),

            "name":

                name,

            "status":

                "running",

            "created":

                datetime.utcnow().isoformat()

        }

        self.test_runs.append(cycle)

        return cycle

    def record_result(

        self,

        cycle_id,

        test_name,

        status

    ):

        result = {

            "cycle_id":

                cycle_id,

            "test":

                test_name,

            "status":

                status

        }

        if status == "failed":

            self.failures.append(result)

        return result

    def complete_cycle(

        self,

        cycle_id

    ):

        for cycle in self.test_runs:

            if cycle["id"] == cycle_id:

                cycle["status"] = "completed"

                return cycle

        return None

    def generate_health_report(self):

        return {

            "total_cycles":

                len(self.test_runs),

            "failures":

                len(self.failures),

            "status":

                "healthy"

                if len(self.failures) == 0

                else "attention_required"

        }