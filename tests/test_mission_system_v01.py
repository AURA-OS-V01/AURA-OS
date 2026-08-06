from core.self_builder.mission_system_v01 import (

    MissionSystem

)

def test_mission_system():

    system = MissionSystem()

    mission = system.create_mission(

        "Build AURA client dashboard"

    )

    result = system.update_status(

        mission["id"],

        "planning"

    )

    print("Mission System Test")

    print("------------------")

    print(result)

if __name__ == "__main__":

    test_mission_system()