from agents.product.documentation_generator_v01 import (

    DocumentationGenerator

)

def test_documentation_generator():

    generator = DocumentationGenerator()

    result = generator.generate(

        "Fitness App"

    )

    print("Documentation Generator Test")

    print("----------------------------")

    print(result)

if __name__ == "__main__":

    test_documentation_generator()