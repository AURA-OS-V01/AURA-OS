from uuid import uuid4

class AURADatabaseConnector:

    def __init__(self):

        self.records = []

    def insert(

        self,

        collection,

        data

    ):

        record = {

            "id":

                str(uuid4()),

            "collection":

                collection,

            "data":

                data

        }

        self.records.append(record)

        return record

    def query(

        self,

        collection

    ):

        return [

            record

            for record in self.records

            if record["collection"] == collection

        ]