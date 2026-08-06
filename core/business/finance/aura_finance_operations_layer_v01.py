from uuid import uuid4

from datetime import datetime

class AURAFinanceOperationsLayer:

    def __init__(self):

        self.transactions = []

    def record_transaction(

        self,

        transaction_type,

        description,

        amount

    ):

        transaction = {

            "id":

                str(uuid4()),

            "type":

                transaction_type,

            "description":

                description,

            "amount":

                amount,

            "created":

                datetime.utcnow().isoformat()

        }

        self.transactions.append(

            transaction

        )

        return transaction

    def calculate_summary(self):

        revenue = 0

        expenses = 0

        for transaction in self.transactions:

            if transaction["type"] == "revenue":

                revenue += transaction["amount"]

            elif transaction["type"] == "expense":

                expenses += transaction["amount"]

        return {

            "revenue":

                revenue,

            "expenses":

                expenses,

            "profit":

                revenue - expenses

        }

    def get_finance_data(self):

        return {

            "transactions":

                self.transactions,

            "summary":

                self.calculate_summary()

        }