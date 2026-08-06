class CapabilityRouter:

    """

    Selects agents based on capabilities.

    """

    def __init__(

        self,

        registry

    ):

        self.registry = registry

    def route(

        self,

        required_capability: str

    ):

        agents = self.registry.find_agents(

            required_capability

        )

        return {

            "capability": required_capability,

            "agents": agents

        }