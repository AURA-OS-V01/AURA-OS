class MissionEvaluator:

    """

    Evaluates completed AURA missions.

    """

    def __init__(self):

        self.evaluations = []

    def evaluate(

        self,

        mission_name: str,

        success: bool,

        lessons: list

    ):

        evaluation = {

            "mission": mission_name,

            "success": success,

            "lessons": lessons

        }

        self.evaluations.append(evaluation)

        return evaluation

    def get_evaluations(self):

        return self.evaluations