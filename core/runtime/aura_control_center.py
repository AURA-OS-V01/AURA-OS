
class AURAControlCenter:

    def render(self, boot):

        print()

        print("=" * 60)

        print("                 AURA OS v1.0")

        print("=" * 60)

        print()

        print("STATUS")

        print("------")

        print("ONLINE")

        print()

        print("SYSTEM")

        print("------")

        print(f"Modules Loaded : {boot['modules']}")

        print(f"Agents Active  : {boot['agents']}")

        print(f"Events Logged  : {boot['events']}")

        print()

        print("DISCOVERY")

        print("---------")

        for group, items in boot["discovered"].items():

            print(f"{group:15} {len(items)}")

        print()

        print("LOADED AGENTS")

        print("-------------")

        for agent in boot["loaded_agents"]:

            print(f"✓ {agent}")

        print()

        print("SYSTEM READY")

        print("=" * 60)

