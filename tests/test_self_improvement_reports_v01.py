from core.self_builder.self_improvement_reports_v01 import (

    SelfImprovementReports

)

def test_reports():

    reports = SelfImprovementReports()

    result = reports.generate(

        [

            "Mission System",

            "Planner System"

        ],

        "Client Platform",

        [

            "Improve monitoring"

        ]

    )

    print("Self Improvement Reports Test")

    print("----------------------------")

    print(result)

if __name__ == "__main__":

    test_reports()