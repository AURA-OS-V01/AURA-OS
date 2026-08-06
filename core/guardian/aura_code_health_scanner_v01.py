import os

from datetime import datetime

class AURACodeHealthScanner:

    def __init__(self):

        self.reports = []

    def scan_directory(

        self,

        path

    ):

        files = []

        for root, directories, filenames in os.walk(path):

            for filename in filenames:

                files.append(

                    os.path.join(

                        root,

                        filename

                    )

                )

        report = {

            "path":

                path,

            "file_count":

                len(files),

            "files":

                files,

            "status":

                "scanned",

            "created":

                datetime.utcnow().isoformat()

        }

        self.reports.append(report)

        return report

    def get_reports(self):

        return self.reports