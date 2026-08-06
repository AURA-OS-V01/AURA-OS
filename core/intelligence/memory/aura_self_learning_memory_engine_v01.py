from uuid import uuid4

from datetime import datetime

class AURASelfLearningMemoryEngine:

    def __init__(self):

        self.experiences = []

        self.learned_patterns = []

    def record_experience(

        self,

        action,

        context

    ):

        experience = {

            "id":

                str(uuid4()),

            "action":

                action,

            "context":

                context,

            "outcome":

                None,

            "created":

                datetime.utcnow().isoformat()

        }

        self.experiences.append(

            experience

        )

        return experience

    def record_outcome(

        self,

        experience_id,

        outcome

    ):

        for experience in self.experiences:

            if experience["id"] == experience_id:

                experience["outcome"] = outcome

                return experience

        return None

    def learn_pattern(

        self,

        observation,

        improvement

    ):

        pattern = {

            "id":

                str(uuid4()),

            "observation":

                observation,

            "improvement":

                improvement,

            "created":

                datetime.utcnow().isoformat()

        }

        self.learned_patterns.append(

            pattern

        )

        return pattern

    def get_memory_state(self):

        return {

            "experiences":

                self.experiences,

            "patterns":

                self.learned_patterns

        }