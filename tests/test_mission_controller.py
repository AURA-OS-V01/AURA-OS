from core.missions.controller import MissionController

from core.orchestrator.aura_orchestrator import AURAOrchestrator

from core.routing.agent_router import AgentRouter

from core.workflow.workflow_manager import WorkflowManager

def test_controller():

    controller = MissionController(

        AURAOrchestrator(),

        AgentRouter(),

        WorkflowManager()

    )

    result = controller.run_mission(

        "AI Business Discovery",

        "Find a profitable AI business opportunity"

    )

    print("Mission Controller Test")

    print("----------------------")

    print(result)

if __name__ == "__main__":

    test_controller()