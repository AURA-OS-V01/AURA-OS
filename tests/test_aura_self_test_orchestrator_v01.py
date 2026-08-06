from core.guardian.aura_self_test_orchestrator_v01 import (

    AURASelfTestOrchestrator

)

def test_self_test_orchestrator():

    system = AURASelfTestOrchestrator()

    cycle = system.start_test_cycle(

        "AURA Full System Test"

    )

    system.record_result(

        cycle["id"],

        "CRM Test",

        "passed"

    )

    system.record_result(

        cycle["id"],

        "Payment Test",

        "passed"

    )

    completed = system.complete_cycle(

        cycle["id"]

    )

    report = system.generate_health_report()

    print(

        "AURA Self-Test Orchestrator Test"

    )

    print(

        "--------------------------------"

    )

    print(completed)

    print(report)

    assert completed["status"] == (

        "completed"

    )

    assert report["status"] == (

        "healthy"

    )

if __name__ == "__main__":

    test_self_test_orchestrator()