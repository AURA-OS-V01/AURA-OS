from uuid import uuid4

class Identity:

    """

    Represents an AURA user identity.

    """

    def __init__(

        self,

        name: str,

        role: str

    ):

        self.id = str(uuid4())

        self.name = name

        self.role = role

    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "role": self.role

        }