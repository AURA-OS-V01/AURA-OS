class MissionPlanner:

    """

    Creates agent teams for missions.

    """

    def __init__(

        self,

        selector

    ):

        self.selector = selector

    def create_plan(

        self,

        mission,

        required_capabilities

    ):

        team = []

        for capability in required_capabilities:

            agent = self.selector.select(

                capability

            )

            if agent:

                team.append(agent)

        return {

            "mission": mission,

            "team": team,

            "status": "planned"

        }