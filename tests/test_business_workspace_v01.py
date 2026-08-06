from aura_platform.workspaces.business_workspace_v01 import (

    BusinessWorkspace

)

def test_business_workspace():

    workspace = BusinessWorkspace()

    result = workspace.create_workspace(

        "Example AI Ltd"

    )

    print("Business Workspace Test")

    print("----------------------")

    print(result)

if __name__ == "__main__":

    test_business_workspace()