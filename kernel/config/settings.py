import os

class AuraSettings:

    """

    Central configuration manager for AURA.

    """

    def __init__(self):

        self.name = "AURA"

        self.version = "1.0"

        self.environment = os.getenv(

            "AURA_ENV",

            "development"

        )

        self.security_level = "maximum"

        self.owner_mode = True

    def to_dict(self):

        return {

            "name": self.name,

            "version": self.version,

            "environment": self.environment,

            "security_level": self.security_level,

            "owner_mode": self.owner_mode

        }