from uuid import uuid4

from datetime import datetime

class AURAAgentSimulationTestingEnvironment:

    def __init__(self):

        self.scenarios = []

        self.results = []

    def create_scenario(

        self,

        name,

        description

    ):

        scenario = {

            "id":

                str(uuid4()),

            "name":

                name,

            "description":

                description,

            "created":

                datetime.utcnow().isoformat()

        }

        self.scenarios.append(

            scenario

        )

        return scenario

    def run_simulation(

        self,

        agent_id,

        scenario_id,

        performance_score

    ):

        result = {

            "id":

                str(uuid4()),

            "agent_id":

                agent_id,

            "scenario_id":

                scenario_id,

            "score":

                performance_score,

            "status":

                "completed",

            "created":

                datetime.utcnow().isoformat()

        }

        self.results.append(

            result

        )

        return result

    def evaluate_agent(

        self,

        agent_id

    ):

        tests = [

            result

            for result in self.results

            if result["agent_id"] == agent_id

        ]

        if not tests:

            return None

        average = (

            sum(

                test["score"]

                for test in tests

            )

            /

            len(tests)

        )

        return {

            "agent_id":

                agent_id,

            "average_score":

                average,

            "tests":

                len(tests)

        }

    def get_results(self):

        return self.results