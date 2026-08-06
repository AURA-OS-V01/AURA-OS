class PerformanceTracker:

    """

    Tracks agent performance metrics.

    """

    def __init__(self):

        self.performance = {}

    def register_agent(

        self,

        agent: str

    ):

        self.performance[agent] = {

            "tasks_completed": 0,

            "successful_tasks": 0,

            "success_rate": 0

        }

        return self.performance[agent]

    def record_result(

        self,

        agent: str,

        success: bool

    ):

        if agent not in self.performance:

            self.register_agent(agent)

        data = self.performance[agent]

        data["tasks_completed"] += 1

        if success:

            data["successful_tasks"] += 1

        data["success_rate"] = (

            data["successful_tasks"]

            /

            data["tasks_completed"]

        )

        return data

    def get_score(

        self,

        agent: str

    ):

        return self.performance.get(

            agent

        )