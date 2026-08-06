from uuid import uuid4

from datetime import datetime

class AURAPaymentIntegration:

    def __init__(self):

        self.providers = []

        self.transactions = []

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

    def create_transaction(

        self,

        provider_id,

        client,

        amount,

        currency

    ):

        transaction = {

            "id":

                str(uuid4()),

            "provider_id":

                provider_id,

            "client":

                client,

            "amount":

                amount,

            "currency":

                currency,

            "status":

                "pending",

            "created":

                datetime.utcnow().isoformat()

        }

        self.transactions.append(transaction)

        return transaction

    def update_transaction_status(

        self,

        transaction_id,

        status

    ):

        for transaction in self.transactions:

            if transaction["id"] == transaction_id:

                transaction["status"] = status

                return transaction

        return None

    def get_transactions(self):

        return self.transactions