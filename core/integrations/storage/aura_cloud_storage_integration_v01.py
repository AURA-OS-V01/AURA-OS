from uuid import uuid4

from datetime import datetime

class AURACloudStorageIntegration:

    def __init__(self):

        self.providers = []

        self.files = []

    def connect_provider(

        self,

        provider,

        account

    ):

        connection = {

            "id":

                str(uuid4()),

            "provider":

                provider,

            "account":

                account,

            "status":

                "connected",

            "created":

                datetime.utcnow().isoformat()

        }

        self.providers.append(connection)

        return connection

    def upload_file(

        self,

        provider_id,

        filename,

        file_type

    ):

        file_record = {

            "id":

                str(uuid4()),

            "provider_id":

                provider_id,

            "filename":

                filename,

            "type":

                file_type,

            "status":

                "stored",

            "created":

                datetime.utcnow().isoformat()

        }

        self.files.append(file_record)

        return file_record

    def get_files(self):

        return self.files