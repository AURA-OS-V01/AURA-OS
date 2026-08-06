from core.integration.planner_connector import PlannerConnector

from core.workflow.workflow_manager import WorkflowManager

from agents.collaboration.collaboration_manager import CollaborationManager

from agents.communication.message_bus import MessageBus

from agents.workspace.workspace import AgentWorkspace

from agents.results.result_exchange import ResultExchange

def test_connector():

    collaboration = CollaborationManager(

        MessageBus(),

        AgentWorkspace(),

        ResultExchange()

    )

    connector = PlannerConnector(

        WorkflowManager(),

        collaboration

    )

    plan = {

        "mission": "AI Business Analysis",

        "team": [

            {

                "agent": "Research Agent"

            },

            {

                "agent": "Finance Agent"

            },

            {

                "agent": "Security Agent"

            }

        ]

    }

    result = connector.execute_plan(

        plan

    )

    print("Planner Connector Test")

    print("---------------------")

    print(result)

if __name__ == "__main__":

    test_connector()