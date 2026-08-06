from core.runtime.aura_module_registry_v01 import (

    AURAModuleRegistry

)

def test_module_registry():

    registry = AURAModuleRegistry()

    module = registry.register(

        "Planning Agent",

        "agent",

        "Strategic planning"

    )

    found = registry.get_module(

        "Planning Agent"

    )

    modules = registry.list_modules()

    state = registry.get_state()

    assert module["status"] == "registered"

    assert found["name"] == "Planning Agent"

    assert len(modules) == 1

    assert state["total"] == 1

    assert registry.unregister(

        "Planning Agent"

    ) is True

    assert registry.count() == 0

if __name__ == "__main__":

    test_module_registry()