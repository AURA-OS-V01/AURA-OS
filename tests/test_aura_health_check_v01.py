from core.runtime.aura_unified_intelligence_runtime_v01 import (

    AURAUnifiedIntelligenceRuntime

)

from core.runtime.aura_health_check_v01 import (

    AURAHealthCheck

)

def test_health_check():

    runtime = AURAUnifiedIntelligenceRuntime()

    runtime.register_module(

        "Reasoning Engine",

        "Decision making"

    )

    health = AURAHealthCheck(

        runtime

    )

    result = health.run()

    assert result["status"] == "healthy"

    assert result["checks"]["runtime"] is True

    assert result["checks"]["modules"] is True

    assert result["checks"]["executions"] is True

    assert result["checks"]["optimization"] is True

    assert result["checks"]["evolution"] is True

if __name__ == "__main__":

    test_health_check()