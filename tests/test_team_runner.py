from core.missions.team_runner import TeamMissionRunner

from agents.collaboration.collaboration_manager import CollaborationManager

from agents.communication.message_bus import MessageBus

from agents.workspace.workspace import AgentWorkspace

from agents.results.result_exchange import ResultExchange

def test_team_runner():

    collaboration = CollaborationManager(

        MessageBus(),

        AgentWorkspace(),

        ResultExchange()

    )

    runner = TeamMissionRunner(

        collaboration

    )

    result = runner.run(

        "AI_business_analysis",

        [

            "Research Agent",

            "Finance Agent",

            "Marketing Agent",

            "Security Agent"

        ]

    )

    print("Team Mission Runner Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_team_runner()