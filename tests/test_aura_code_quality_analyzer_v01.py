from core.guardian.aura_code_quality_analyzer_v01 import (

    AURACodeQualityAnalyzer

)

def test_code_quality_analyzer():

    analyzer = AURACodeQualityAnalyzer()

    report = analyzer.analyze_file(

        "core/guardian/aura_code_quality_analyzer_v01.py"

    )

    print(

        "AURA Code Quality Analyzer Test"

    )

    print(

        "--------------------------------"

    )

    print(report)

    assert report["total_lines"] > 0

    assert report["quality_score"] >= 0

if __name__ == "__main__":

    test_code_quality_analyzer()