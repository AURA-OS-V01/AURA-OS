from datetime import datetime

from uuid import uuid4

class AURAAgentSelfOptimizationEngine:

    def __init__(self):

        self.metrics = []

        self.improvements = []

    def record_performance(self, system, score, notes=""):

        metric = {

            "id": str(uuid4()),

            "system": system,

            "score": score,

            "notes": notes,

            "created": datetime.utcnow().isoformat()

        }

        self.metrics.append(metric)

        return metric

    def analyze(self, metric_id):

        for metric in self.metrics:

            if metric["id"] == metric_id:

                if metric["score"] < 50:

                    recommendation = "Major improvement required"

                elif metric["score"] < 80:

                    recommendation = "Optimize performance"

                else:

                    recommendation = "System performing well"

                return {

                    "metric_id": metric_id,

                    "recommendation": recommendation

                }

        return None

    def create_improvement(self, target, change):

        improvement = {

            "id": str(uuid4()),

            "target": target,

            "change": change,

            "status": "proposed",

            "created": datetime.utcnow().isoformat()

        }

        self.improvements.append(improvement)

        return improvement

    def apply_improvement(self, improvement_id):

        for item in self.improvements:

            if item["id"] == improvement_id:

                item["status"] = "applied"

                return item

        return None

    def get_state(self):

        return {

            "metrics": self.metrics,

            "improvements": self.improvements

        }