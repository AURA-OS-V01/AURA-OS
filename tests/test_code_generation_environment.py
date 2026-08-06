from core.development.generation.code_generator import (

    CodeGenerationEnvironment

)

def test_code_generation():

    generator = CodeGenerationEnvironment()

    result = generator.create_change(

        {

            "objective":

            "Improve memory retrieval"

        },

        [

            "core/memory.py",

            "tests/test_memory.py"

        ]

    )

    print("Code Generation Environment Test")

    print("--------------------------------")

    print(result)

if __name__ == "__main__":

    test_code_generation()