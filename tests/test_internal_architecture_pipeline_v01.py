from core.self_builder.internal_architecture_pipeline_v01 import (

    InternalArchitecturePipeline

)

def test_internal_architecture_pipeline():

    pipeline = InternalArchitecturePipeline()

    result = pipeline.generate(

        "Build AURA client dashboard"

    )

    print("Internal Architecture Pipeline Test")

    print("----------------------------------")

    print(result)

if __name__ == "__main__":

    test_internal_architecture_pipeline()