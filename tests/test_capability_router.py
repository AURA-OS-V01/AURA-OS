from agents.registry.capability_registry import CapabilityRegistry

from core.routing.capability_router import CapabilityRouter

def test_router():

    registry = CapabilityRegistry()

    registry.register_agent(

        "Finance Agent",

        [

            "financial_analysis",

            "forecasting"

        ],

        [

            "read_workspace"

        ]

    )

    registry.register_agent(

        "Marketing Agent",

        [

            "customer_analysis"

        ],

        [

            "create_reports"

        ]

    )

    router = CapabilityRouter(

        registry

    )

    result = router.route(

        "financial_analysis"

    )

    print("Capability Router Test")

    print("---------------------")

    print(result)

if __name__ == "__main__":

    test_router()