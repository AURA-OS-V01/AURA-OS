from uuid import uuid4

from datetime import datetime

class AURABusinessAnalyticsDashboard:

    def __init__(self):

        self.metrics = []

        self.reports = []

    def record_metric(

        self,

        category,

        metric_name,

        value

    ):

        metric = {

            "id":

                str(uuid4()),

            "category":

                category,

            "name":

                metric_name,

            "value":

                value,

            "created":

                datetime.utcnow().isoformat()

        }

        self.metrics.append(

            metric

        )

        return metric

    def generate_report(

        self,

        category

    ):

        category_metrics = [

            metric

            for metric in self.metrics

            if metric["category"] == category

        ]

        total = sum(

            metric["value"]

            for metric in category_metrics

        )

        report = {

            "id":

                str(uuid4()),

            "category":

                category,

            "total":

                total,

            "metric_count":

                len(category_metrics),

            "created":

                datetime.utcnow().isoformat()

        }

        self.reports.append(

            report

        )

        return report

    def get_dashboard_data(self):

        return {

            "metrics":

                self.metrics,

            "reports":

                self.reports

        }