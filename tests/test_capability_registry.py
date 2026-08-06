from agents.registry.capability_registry import CapabilityRegistry

def test_registry():

    registry = CapabilityRegistry()

    registry.register_agent(

        "Research Agent",

        [

            "market_analysis",

            "trend_detection"

        ],

        [

            "read_workspace",

            "create_reports"

        ]

    )

    registry.register_agent(

        "Security Agent",

        [

            "risk_analysis",

            "security_review"

        ],

        [

            "audit_systems"

        ]

    )

    result = registry.find_agents(

        "risk_analysis"

    )

    print("Capability Registry Test")

    print("-----------------------")

    print(result)

if __name__ == "__main__":

    test_registry()