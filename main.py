
from core.runtime.aura_bootstrap_orchestrator_v01 import (

    AURABootstrapOrchestrator

)

print("=" * 60)

print("AURA OS STARTING")

print("=" * 60)

aura = AURABootstrapOrchestrator()

result = aura.start()

print("\nBOOT RESULT:")

print(result)

