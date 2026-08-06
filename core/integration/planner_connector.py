class PlannerConnector:

    """

    Connects mission planning

    with mission execution.

    """

    def __init__(

        self,

        workflow_manager,

        collaboration_manager

    ):

        self.workflow = workflow_manager

        self.collaboration = collaboration_manager

    def execute_plan(

        self,

        plan

    ):

        mission = plan["mission"]

        agents = []

        for item in plan["team"]:

            agents.append(

                item["agent"]

            )

        workflow = self.workflow.create_workflow(

            mission,

            agents

        )

        collaboration = (

            self.collaboration.start_collaboration(

                mission,

                agents

            )

        )

        return {

            "mission": mission,

            "agents": agents,

            "workflow": workflow,

            "collaboration": collaboration,

            "status": "started"

        }