from core.runtime.aura_bootstrap_orchestrator_v01 import (

    AURABootstrapOrchestrator

)

def test_bootstrap_orchestrator():

    aura = AURABootstrapOrchestrator()

    result = aura.start()

    status = aura.get_status()

    assert result["status"] == "online"

    assert result["health"]["status"] == "healthy"

    assert status["runtime_loaded"] is True

if __name__ == "__main__":

    test_bootstrap_orchestrator()