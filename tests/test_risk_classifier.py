from core.risk.risk_classifier import RiskClassifier

def test_risk():

    classifier = RiskClassifier()

    research = classifier.classify(

        [

            "research",

            "read"

        ]

    )

    deployment = classifier.classify(

        [

            "code_execution",

            "system_change"

        ]

    )

    print("Risk Classifier Test")

    print("--------------------")

    print(research)

    print(deployment)

if __name__ == "__main__":

    test_risk()