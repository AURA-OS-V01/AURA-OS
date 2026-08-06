from agents.core.agent import Agent

class DeveloperAgent(Agent):

    """

    AURA software development specialist.

    """

    def __init__(self):

        super().__init__(

            "AURA Developer Agent",

            "developer_specialist"

        )

        self.permissions = [

            "analyze_code",

            "build_features",

            "run_tests"

        ]

        self.projects = []

    def create_task(

        self,

        project: str

    ):

        task = {

            "project": project,

            "status": "planned"

        }

        self.projects.append(task)

        return task

    def get_projects(self):

        return self.projects