from core.interface.adapters.aura_capability_execution_adapter_v01 import (

    AURACapabilityExecutionAdapter

)

def test_capability_execution_adapter():

    adapter = AURACapabilityExecutionAdapter()

    result = adapter.execute(

        "Research Agent",

        "Analyze AI market opportunity"

    )

    state = adapter.get_state()

    print(

        "AURA Capability Execution Adapter Test"

    )

    print(state)

    assert result["status"] == (

        "completed"

    )

    assert result["capability"] == (

        "Research Agent"

    )

    assert len(

        state["executions"]

    ) == 1

if __name__ == "__main__":

    test_capability_execution_adapter()