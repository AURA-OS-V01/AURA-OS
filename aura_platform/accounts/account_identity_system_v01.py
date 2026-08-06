from uuid import uuid4

from datetime import datetime

class AccountIdentitySystem:

    """

    Manages AURA user identities.

    """

    def __init__(self):

        self.accounts = []

    def create_account(

        self,

        account_type

    ):

        account = {

            "id": str(uuid4()),

            "type": account_type,

            "status": "active",

            "created":

                datetime.utcnow().isoformat()

        }

        self.accounts.append(

            account

        )

        return account