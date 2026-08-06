from uuid import uuid4

from datetime import datetime

class AURAPredictiveIntelligenceEngine:

    def __init__(self):

        self.predictions = []

        self.scenarios = []

    def create_prediction(

        self,

        subject,

        expected_outcome,

        confidence

    ):

        prediction = {

            "id":

                str(uuid4()),

            "subject":

                subject,

            "expected_outcome":

                expected_outcome,

            "confidence":

                confidence,

            "created":

                datetime.utcnow().isoformat()

        }

        self.predictions.append(

            prediction

        )

        return prediction

    def create_scenario(

        self,

        name,

        description,

        probability

    ):

        scenario = {

            "id":

                str(uuid4()),

            "name":

                name,

            "description":

                description,

            "probability":

                probability,

            "created":

                datetime.utcnow().isoformat()

        }

        self.scenarios.append(

            scenario

        )

        return scenario

    def evaluate_prediction(

        self,

        prediction_id

    ):

        for prediction in self.predictions:

            if prediction["id"] == prediction_id:

                if prediction["confidence"] >= 80:

                    prediction["status"] = "high_confidence"

                elif prediction["confidence"] >= 50:

                    prediction["status"] = "medium_confidence"

                else:

                    prediction["status"] = "low_confidence"

                return prediction

        return None

    def get_prediction_state(self):

        return {

            "predictions":

                self.predictions,

            "scenarios":

                self.scenarios

        }