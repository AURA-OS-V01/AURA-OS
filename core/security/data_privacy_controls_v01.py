from uuid import uuid4

from datetime import datetime

class DataPrivacyControls:

    """

    Manages user privacy preferences.

    """

    def __init__(self):

        self.preferences = []

    def create_privacy_profile(

        self,

        user_id,

        memory_enabled,

        analytics_enabled,

        data_storage_level

    ):

        profile = {

            "id": str(uuid4()),

            "user_id": user_id,

            "memory_enabled": memory_enabled,

            "analytics_enabled": analytics_enabled,

            "data_storage_level": data_storage_level,

            "created":

                datetime.utcnow().isoformat()

        }

        self.preferences.append(profile)

        return profile

    def get_profile(

        self,

        user_id

    ):

        for profile in self.preferences:

            if profile["user_id"] == user_id:

                return profile

        return None