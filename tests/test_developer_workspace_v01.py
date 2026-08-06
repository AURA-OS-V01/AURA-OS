from aura_platform.developer.developer_workspace_v01 import (

    DeveloperWorkspace

)

def test_developer_workspace():

    workspace = DeveloperWorkspace()

    result = workspace.create_project(

        "Mobile Application",

        "Python"

    )

    print("Developer Workspace Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_developer_workspace()