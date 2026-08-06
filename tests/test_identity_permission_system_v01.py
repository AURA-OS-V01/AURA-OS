from core.security.identity_permission_system_v01 import (

    IdentityPermissionSystem

)

def test_identity_permissions():

    system = IdentityPermissionSystem()

    system.create_identity(

        "admin_user",

        "Administrator",

        [

            "manage_workspace",

            "view_reports"

        ]

    )

    result = system.check_permission(

        "admin_user",

        "manage_workspace"

    )

    print("Identity Permission Test")

    print("-----------------------")

    print(result)

if __name__ == "__main__":

    test_identity_permissions()