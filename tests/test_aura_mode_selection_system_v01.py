from core.interface.aura_mode_selection_system_v01 import (

    AURAModeSelectionSystem

)

def test_mode_selection():

    system = AURAModeSelectionSystem()

    result = system.select_mode(

        "Test User",

        "Coding"

    )

    print("AURA Mode Selection Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_mode_selection()