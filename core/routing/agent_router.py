class AgentRouter:

    """

    Determines which AURA agents

    should handle a task.

    """

    def __init__(self):

        self.rules = {

            "code": ["Developer Agent"],

            "security": ["Security Agent"],

            "business": [

                "Research Agent",

                "Marketing Agent",

                "Finance Agent"

            ],

            "strategy": [

                "Owner Agent"

            ]

        }

    def route(

        self,

        task: str

    ):

        task_lower = task.lower()

        selected = []

        for keyword, agents in self.rules.items():

            if keyword in task_lower:

                selected.extend(agents)

        if not selected:

            selected.append("Owner Agent")

        return {

            "task": task,

            "agents": selected

        }