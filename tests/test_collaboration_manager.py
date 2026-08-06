from agents.collaboration.collaboration_manager import CollaborationManager

from agents.communication.message_bus import MessageBus

from agents.workspace.workspace import AgentWorkspace

from agents.results.result_exchange import ResultExchange

def test_collaboration():

    manager = CollaborationManager(

        MessageBus(),

        AgentWorkspace(),

        ResultExchange()

    )

    mission = manager.start_collaboration(

        "mission_001",

        [

            "Research Agent",

            "Finance Agent",

            "Marketing Agent"

        ]

    )

    result = manager.submit_agent_result(

        "Research Agent",

        "Market research",

        {

            "finding": "AI automation demand increasing"

        },

        0.9

    )

    message = manager.notify_agent(

        "Research Agent",

        "Finance Agent",

        "Research complete. Review findings."

    )

    print("Collaboration Manager Test")

    print("--------------------------")

    print(mission)

    print(result)

    print(message)

if __name__ == "__main__":

    test_collaboration()