from core.guardian.aura_test_failure_analyzer_v01 import (

    AURATestFailureAnalyzer

)

def test_failure_analyzer():

    analyzer = AURATestFailureAnalyzer()

    analyzer.record_test_result(

        "CRM Test",

        "passed"

    )

    failure = analyzer.record_failure(

        "Payment Test",

        "AssertionError",

        "Expected completed status"

    )

    report = analyzer.generate_report()

    print(

        "AURA Test Failure Analyzer Test"

    )

    print(

        "--------------------------------"

    )

    print(failure)

    print(report)

    assert failure["category"] == (

        "logic"

    )

    assert report["total_failures"] == 1

if __name__ == "__main__":

    test_failure_analyzer()