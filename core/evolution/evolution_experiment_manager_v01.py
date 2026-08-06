from uuid import uuid4

from datetime import datetime

class EvolutionExperimentManager:

    """

    Creates and tracks improvement experiments.

    """

    def __init__(self):

        self.experiments = []

    def create_experiment(

        self,

        objective,

        change

    ):

        experiment = {

            "id": str(uuid4()),

            "objective": objective,

            "change": change,

            "status": "running",

            "created":

                datetime.utcnow().isoformat()

        }

        self.experiments.append(

            experiment

        )

        return experiment

    def complete(

        self,

        experiment_id,

        success

    ):

        for experiment in self.experiments:

            if experiment["id"] == experiment_id:

                experiment["status"] = (

                    "accepted"

                    if success

                    else

                    "rejected"

                )

                return experiment

        return None