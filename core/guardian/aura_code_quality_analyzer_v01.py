import os

from datetime import datetime

class AURACodeQualityAnalyzer:

    def __init__(self):

        self.reports = []

    def analyze_file(

        self,

        filepath

    ):

        with open(

            filepath,

            "r",

            encoding="utf-8"

        ) as file:

            lines = file.readlines()

        total_lines = len(lines)

        empty_lines = len(

            [

                line

                for line in lines

                if not line.strip()

            ]

        )

        report = {

            "file":

                filepath,

            "total_lines":

                total_lines,

            "empty_lines":

                empty_lines,

            "quality_score":

                self.calculate_score(

                    total_lines,

                    empty_lines

                ),

            "created":

                datetime.utcnow().isoformat()

        }

        self.reports.append(report)

        return report

    def calculate_score(

        self,

        total_lines,

        empty_lines

    ):

        if total_lines == 0:

            return 100

        ratio = empty_lines / total_lines

        score = 100 - int(

            ratio * 20

        )

        if score < 0:

            score = 0

        return score

    def analyze_directory(

        self,

        directory

    ):

        results = []

        for root, folders, files in os.walk(directory):

            for filename in files:

                if filename.endswith(".py"):

                    results.append(

                        self.analyze_file(

                            os.path.join(

                                root,

                                filename

                            )

                        )

                    )

        return results

    def get_reports(self):

        return self.reports