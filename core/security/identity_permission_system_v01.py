from uuid import uuid4

from datetime import datetime

class IdentityPermissionSystem:

    """

    Manages user identities and permissions.

    """

    def __init__(self):

        self.users = []

    def create_identity(

        self,

        username,

        role,

        permissions

    ):

        identity = {

            "id": str(uuid4()),

            "username": username,

            "role": role,

            "permissions": permissions,

            "status": "active",

            "created":

                datetime.utcnow().isoformat()

        }

        self.users.append(identity)

        return identity

    def check_permission(

        self,

        username,

        permission

    ):

        for user in self.users:

            if user["username"] == username:

                return permission in user["permissions"]

        return False