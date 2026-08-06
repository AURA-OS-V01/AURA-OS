from uuid import uuid4

from datetime import datetime

class AURAPredictiveIntelligenceEngine:

    def __init__(self):

        self.datasets = []

    def create_dataset(

        self,

        name

    ):

        dataset = {

            "id":

                str(uuid4()),

            "name":

                name,

            "values":

                [],

            "created":

                datetime.utcnow().isoformat()

        }

        self.datasets.append(dataset)

        return dataset

    def add_value(

        self,

        dataset_id,

        value

    ):

        for dataset in self.datasets:

            if dataset["id"] == dataset_id:

                dataset["values"].append(

                    value

                )

                return dataset

        return None

    def predict_trend(

        self,

        dataset_id

    ):

        for dataset in self.datasets:

            if dataset["id"] == dataset_id:

                values = dataset["values"]

                if len(values) < 2:

                    return "insufficient_data"

                if values[-1] > values[-2]:

                    return "growth"

                elif values[-1] < values[-2]:

                    return "decline"

                return "stable"

        return None

    def get_datasets(self):

        return self.datasets