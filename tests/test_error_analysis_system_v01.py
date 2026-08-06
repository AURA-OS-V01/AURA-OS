from core.learning.error_analysis_system_v01 import (

    ErrorAnalysisSystem

)

def test_error_analysis():

    system = ErrorAnalysisSystem()

    result = system.record_error(

        "Accuracy",

        "Answer lacked sufficient verification",

        "High"

    )

    print("Error Analysis Test")

    print("-------------------")

    print(result)

if __name__ == "__main__":

    test_error_analysis()