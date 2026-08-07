
from pathlib import Path

class AURAAutodiscoveryEngine:

    def __init__(self, registry, event_bus):

        self.registry = registry

        self.event_bus = event_bus

    def discover_directory(self, directory, module_type):

        root = Path(directory)

        if not root.exists():

            return []

        discovered = []

        for file in root.rglob("*.py"):

            if file.name.startswith("__"):

                continue

            module_name = file.stem

            self.registry.register(

                module_name,

                module_type,

                str(file)

            )

            self.event_bus.publish(

                "module.discovered",

                {

                    "name": module_name,

                    "type": module_type,

                    "path": str(file)

                }

            )

            discovered.append(module_name)

        return discovered

    def scan(self):

        results = {}

        results["agents"] = self.discover_directory(

            "agents",

            "agent"

        )

        results["intelligence"] = self.discover_directory(

            "intelligence",

            "intelligence"

        )

        results["memory"] = self.discover_directory(

            "memory",

            "memory"

        )

        results["security"] = self.discover_directory(

            "security",

            "security"

        )

        results["tools"] = self.discover_directory(

            "tools",

            "tool"

        )

        return results

