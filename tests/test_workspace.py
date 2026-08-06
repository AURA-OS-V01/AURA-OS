from agents.workspace.workspace import AgentWorkspace

def test_workspace():

    workspace = AgentWorkspace()

    file = workspace.store(

        "mission_001",

        "Research Agent",

        "market_analysis",

        {

            "market": "AI automation",

            "potential": "high"

        }

    )

    print("Workspace Test")

    print("--------------")

    print(file)

    print(

        workspace.get_mission_files(

            "mission_001"

        )

    )

if __name__ == "__main__":

    test_workspace()