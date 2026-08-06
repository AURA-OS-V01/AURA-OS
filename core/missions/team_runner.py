class TeamMissionRunner:

    """

    Runs multi-agent missions.

    """

    def __init__(

        self,

        collaboration_manager

    ):

        self.collaboration = collaboration_manager

    def run(

        self,

        mission_id: str,

        agents: list

    ):

        mission = self.collaboration.start_collaboration(

            mission_id,

            agents

        )

        return {

            "mission": mission,

            "agents": agents,

            "status": "running"

        }