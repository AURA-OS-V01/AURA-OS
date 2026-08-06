from uuid import uuid4

from datetime import datetime

class AURAAgentLearningEngine:

    def __init__(self):

        self.experiences = []

    def record_experience(

        self,

        agent_id,

        task,

        outcome,

        score

    ):

        experience = {

            "id":

                str(uuid4()),

            "agent_id":

                agent_id,

            "task":

                task,

            "outcome":

                outcome,

            "score":

                score,

            "created":

                datetime.utcnow().isoformat()

        }

        self.experiences.append(

            experience

        )

        return experience

    def evaluate_agent(

        self,

        agent_id

    ):

        agent_experiences = [

            experience

            for experience in self.experiences

            if experience["agent_id"] == agent_id

        ]

        if not agent_experiences:

            return None

        total = sum(

            experience["score"]

            for experience in agent_experiences

        )

        average = (

            total /

            len(agent_experiences)

        )

        return {

            "agent_id":

                agent_id,

            "average_score":

                average,

            "experiences":

                len(agent_experiences)

        }

    def get_experiences(self):

        return self.experiences