from core.learning.capability_expansion_framework_v01 import (

    CapabilityExpansionFramework

)

def test_capability_expansion():

    system = CapabilityExpansionFramework()

    result = system.add_capability(

        "Voice Assistant Mode",

        "Enable hands-free interaction",

        "v1.0"

    )

    print("Capability Expansion Test")

    print("-------------------------")

    print(result)

if __name__ == "__main__":

    test_capability_expansion()