from core.learning.pattern_recognition import (

    PatternRecognitionEngine

)

def test_pattern_engine():

    engine = PatternRecognitionEngine()

    result = engine.analyze(

        [

            {

                "decision":

                "React + FastAPI",

                "outcome":

                "success"

            },

            {

                "decision":

                "React + FastAPI",

                "outcome":

                "success"

            }

        ]

    )

    print("Pattern Recognition Test")

    print("-----------------------")

    print(result)

if __name__ == "__main__":

    test_pattern_engine()