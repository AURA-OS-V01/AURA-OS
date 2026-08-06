from uuid import uuid4

from datetime import datetime

class PersonalizationProfile:

    """

    Stores user personalization settings.

    """

    def __init__(self):

        self.profiles = []

    def create_profile(

        self,

        user_id,

        language,

        explanation_level,

        learning_style

    ):

        profile = {

            "id": str(uuid4()),

            "user_id": user_id,

            "language": language,

            "explanation_level": explanation_level,

            "learning_style": learning_style,

            "created":

                datetime.utcnow().isoformat()

        }

        self.profiles.append(profile)

        return profile