
"""

AURA Kernel v0.1

Core Operating System Kernel

"""

class AuraKernel:

    def __init__(self):

        self.services = {}

        self.state = "INITIALIZED"

    def register(self, name, service):

        self.services[name] = service

        print(f"[REGISTERED] {name}")

    def start_service(self, name):

        print(f"[STARTING] {name}")

    def boot(self):

        print("\n==============================")

        print("      AURA OS BOOTING")

        print("==============================")

        for name in self.services:

            self.start_service(name)

        self.state = "RUNNING"

        print("\n==============================")

        print("      AURA OS READY")

        print("==============================")

    def status(self):

        print(f"\nKernel State: {self.state}")

        print(f"Services: {len(self.services)}")

