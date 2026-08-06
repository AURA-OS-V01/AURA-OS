from governance.constitution.rules import AuraConstitution

from governance.policies.policy_engine import PolicyEngine

def test_policy():

    constitution = AuraConstitution()

    policy = PolicyEngine(

        constitution

    )

    result = policy.evaluate(

        "access_owner_vault",

        {

            "role": "company_agent"

        }

    )

    print("Policy Engine Test")

    print("------------------")

    print(result)

if __name__ == "__main__":

    test_policy()