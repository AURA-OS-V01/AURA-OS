
from core.runtime.aura_module_registry_v01 import (

    AURAModuleRegistry

)

from core.runtime.aura_event_bus_v01 import (

    AURAEventBus

)

from core.agents.aura_agent_lifecycle_manager_v01 import (

    AURAAgentLifecycleManager

)

from core.runtime.aura_agent_management_bridge_v01 import (

    AURAAgentManagementBridge

)

from core.runtime.aura_autodiscovery_engine import (

    AURAAutodiscoveryEngine

)

from core.runtime.aura_agent_loader import (

    AURAAgentLoader

)

from core.mission.aura_mission_system import (

    AURAMissionSystem

)

from core.runtime.aura_evolution_manager import AURAEvolutionManager


class AURARuntimeManager:

    def __init__(self):

        self.registry = AURAModuleRegistry()

        self.event_bus = AURAEventBus()

        self.lifecycle = AURAAgentLifecycleManager()

        self.bridge = AURAAgentManagementBridge(

            self.registry,

            self.lifecycle

        )

        self.discovery = AURAAutodiscoveryEngine(

            self.registry,

            self.event_bus

        )

        self.loader = AURAAgentLoader(

            self.lifecycle

        )

        self.missions = AURAMissionSystem(

            self.bridge

        )

    def boot(self):

        self.event_bus.publish(

            "runtime.started"

        )

        discovered = self.discovery.scan()

        loaded_agents = self.loader.load_directory(

            "agents"

        )

        self.event_bus.publish(

            "runtime.ready",

            {

                "loaded_agents": loaded_agents

            }

        )

        return {

            "modules": self.registry.count(),

            "agents": self.lifecycle.count(),

            "events": len(

                self.event_bus.get_events()

            ),

            "loaded_agents": loaded_agents,

            "discovered": discovered,

            "missions": True

        }

