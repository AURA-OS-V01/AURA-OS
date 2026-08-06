from core.security.safety_policy_framework_v01 import (

    SafetyPolicyFramework

)

def test_safety_policy():

    system = SafetyPolicyFramework()

    system.add_policy(

        "delete_data",

        "Requires administrator approval",

        "restricted"

    )

    result = system.check_action(

        "delete_data"

    )

    print("Safety Policy Framework Test")

    print("---------------------------")

    print(result)

if __name__ == "__main__":

    test_safety_policy()