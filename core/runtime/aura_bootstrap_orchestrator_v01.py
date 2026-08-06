from datetime import datetime, UTC

from core.runtime.aura_unified_intelligence_runtime_v01 import (

    AURAUnifiedIntelligenceRuntime

)

from core.runtime.aura_health_check_v01 import (

    AURAHealthCheck

)

class AURABootstrapOrchestrator:

    def __init__(self):

        self.runtime = None

        self.health = None

        self.status = "offline"

        self.started_at = None

    def start(self):

        self.runtime = AURAUnifiedIntelligenceRuntime()

        self.runtime.register_module(

            "Core Reasoning Engine",

            "Planning and decision support"

        )

        self.runtime.register_module(

            "Self Optimization Engine",

            "Performance improvement"

        )

        self.runtime.register_module(

            "Evolution Engine",

            "System adaptation"

        )

        self.health = AURAHealthCheck(

            self.runtime

        )

        health_result = self.health.run()

        self.status = "online"

        self.started_at = datetime.now(

            UTC

        ).isoformat()

        return {

            "status": self.status,

            "started_at": self.started_at,

            "health": health_result

        }

    def get_status(self):

        return {

            "status": self.status,

            "started_at": self.started_at,

            "runtime_loaded": self.runtime is not None

        }