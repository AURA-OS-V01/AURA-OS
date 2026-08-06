from core.guardian.aura_code_health_scanner_v01 import (

    AURACodeHealthScanner

)

def test_code_health_scanner():

    scanner = AURACodeHealthScanner()

    report = scanner.scan_directory(

        "core"

    )

    print(

        "AURA Code Health Scanner Test"

    )

    print(

        "-----------------------------"

    )

    print(report)

    assert report["status"] == "scanned"

    assert report["file_count"] >= 0

if __name__ == "__main__":

    test_code_health_scanner()