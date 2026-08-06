from core.missions.mission_log import MissionLog

def test_mission_log():

    log = MissionLog()

    mission = log.create_mission(

        "AI Business Discovery",

        "Find profitable AI opportunities"

    )

    log.add_event(

        mission["id"],

        "Research Agent started market analysis"

    )

    result = log.complete_mission(

        mission["id"],

        "Opportunity identified"

    )

    print("Mission Log Test")

    print("----------------")

    print(result)

if __name__ == "__main__":

    test_mission_log()