
class AURAConsole:

    def __init__(self, mission_system):

        self.missions = mission_system

        self.current_mission = None

    def start(self):

        print()

        print("=" * 50)

        print("        AURA MISSION CONSOLE")

        print("=" * 50)

        print("Commands:")

        print(" create <title> <objective>")

        print(" task <agent> <task>")

        print(" run")

        print(" status")

        print(" exit")

        print()

        while True:

            command = input("AURA> ")

            if command == "exit":

                break

            self.handle(command)

    def handle(self, command):

        parts = command.split()

        if not parts:

            return

        if parts[0] == "create":

            title = parts[1]

            objective = " ".join(

                parts[2:]

            )

            self.current_mission = (

                self.missions.create_mission(

                    title,

                    objective

                )

            )

            print(

                "Mission created:",

                self.current_mission["id"]

            )

        elif parts[0] == "task":

            if not self.current_mission:

                print("No active mission")

                return

            agent = parts[1]

            task = " ".join(

                parts[2:]

            )

            result = self.missions.add_task(

                self.current_mission["id"],

                agent,

                task

            )

            print(

                "Task queued:",

                result["id"]

            )

        elif parts[0] == "run":

            result = self.missions.run_next()

            print(result)

        elif parts[0] == "status":

            print(

                self.missions.status()

            )

