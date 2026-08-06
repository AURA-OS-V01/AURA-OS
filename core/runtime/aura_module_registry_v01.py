from datetime import datetime, UTC

from uuid import uuid4

class AURAModuleRegistry:

    def __init__(self):

        self.modules = {}

    def register(

        self,

        name,

        module_type,

        capability

    ):

        module = {

            "id": str(uuid4()),

            "name": name,

            "type": module_type,

            "capability": capability,

            "status": "registered",

            "created": datetime.now(UTC).isoformat()

        }

        self.modules[name] = module

        return module

    def unregister(

        self,

        name

    ):

        if name in self.modules:

            del self.modules[name]

            return True

        return False

    def get_module(

        self,

        name

    ):

        return self.modules.get(

            name

        )

    def list_modules(

        self

    ):

        return list(

            self.modules.values()

        )

    def count(

        self

    ):

        return len(

            self.modules

        )

    def get_state(

        self

    ):

        return {

            "total": len(self.modules),

            "modules": self.modules

        }