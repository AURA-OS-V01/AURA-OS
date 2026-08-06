from core.missions.mission_log import MissionLog

from core.evaluation.mission_evaluator import MissionEvaluator

class MissionController:

    """

    Controls complete AURA missions.

    """

    def __init__(

        self,

        orchestrator,

        router,

        workflow

    ):

        self.orchestrator = orchestrator

        self.router = router

        self.workflow = workflow

        self.log = MissionLog()

        self.evaluator = MissionEvaluator()

    def run_mission(

        self,

        name: str,

        objective: str

    ):

        mission = self.log.create_mission(

            name,

            objective

        )

        self.log.add_event(

            mission["id"],

            "Mission started"

        )

        routing = self.router.route(

            objective

        )

        self.log.add_event(

            mission["id"],

            f"Agents selected: {routing['agents']}"

        )

        workflow = self.workflow.create_workflow(

            name,

            routing["agents"]

        )

        self.log.add_event(

            mission["id"],

            "Workflow created"

        )

        return {

            "mission": mission,

            "routing": routing,

            "workflow": workflow

        }