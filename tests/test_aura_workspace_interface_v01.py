from core.interface.aura_workspace_interface_v01 import (

    AURAWorkspaceInterface

)

def test_workspace():

    system = AURAWorkspaceInterface()

    workspace = system.create_workspace(

        "Test User",

        "Coding"

    )

    system.add_agent(

        workspace["id"],

        "Coding Agent"

    )

    result = system.add_message(

        workspace["id"],

        "Build application"

    )

    print("AURA Workspace Interface Test")

    print("-----------------------------")

    print(result)

if __name__ == "__main__":

    test_workspace()