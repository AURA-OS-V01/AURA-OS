from agents.product.architecture_generator_v01 import (

    ArchitectureGenerator

)

def test_architecture_generator():

    generator = ArchitectureGenerator()

    result = generator.generate(

        "Fitness App"

    )

    print("Architecture Generator Test")

    print("---------------------------")

    print(result)

if __name__ == "__main__":

    test_architecture_generator()