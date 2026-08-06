import os

from uuid import uuid4

from datetime import datetime

class RepositoryScanner:

    """

    Scans repository structure.

    """

    def __init__(self):

        self.scans = []

    def scan(

        self,

        path

    ):

        folders = []

        files = []

        for root, directories, filenames in os.walk(path):

            for directory in directories:

                folders.append(directory)

            for filename in filenames:

                files.append(filename)

        result = {

            "id": str(uuid4()),

            "path": path,

            "folders": folders,

            "files": files,

            "status": "scanned",

            "created":

                datetime.utcnow().isoformat()

        }

        self.scans.append(result)

        return result