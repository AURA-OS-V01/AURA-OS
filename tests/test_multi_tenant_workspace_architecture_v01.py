from core.deployment.multi_tenant_workspace_architecture_v01 import (

    MultiTenantWorkspaceArchitecture

)

def test_multi_tenant():

    system = MultiTenantWorkspaceArchitecture()

    result = system.create_workspace(

        "AURA Research Lab",

        "admin_user",

        "Research"

    )

    print("Multi Tenant Workspace Test")

    print("---------------------------")

    print(result)

if __name__ == "__main__":

    test_multi_tenant()