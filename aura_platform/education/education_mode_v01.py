from uuid import uuid4

from datetime import datetime

class EducationMode:

    """

    Manages personalized learning profiles.

    """

    def __init__(self):

        self.learners = []

    def create_profile(

        self,

        age_range,

        subject,

        level

    ):

        profile = {

            "id": str(uuid4()),

            "age_range": age_range,

            "subject": subject,

            "level": level,

            "teaching_style": self.get_style(age_range),

            "status": "created",

            "created":

                datetime.utcnow().isoformat()

        }

        self.learners.append(

            profile

        )

        return profile

    def get_style(

        self,

        age_range

    ):

        styles = {

            "toddler":

                "visual and simple",

            "child":

                "examples and stories",

            "teen":

                "structured explanations",

            "adult":

                "detailed explanations",

            "professor":

                "advanced analysis"

        }

        return styles.get(

            age_range,

            "adaptive"

        )