
import importlib.util

from pathlib import Path

class AURAAgentLoader:

    def __init__(self, lifecycle_manager):

        self.lifecycle = lifecycle_manager

    def load_directory(self, directory):

        root = Path(directory)

        if not root.exists():

            return []

        loaded = []

        for file in root.rglob("*.py"):

            if file.name.startswith("__"):

                continue

            module_name = file.stem

            try:

                spec = importlib.util.spec_from_file_location(

                    module_name,

                    file

                )

                module = importlib.util.module_from_spec(spec)

                spec.loader.exec_module(module)

                self.lifecycle.register_agent(

                    module_name,

                    "discovered"

                )

                self.lifecycle.activate_agent(

                    module_name

                )

                loaded.append(module_name)

            except Exception:

                continue

        return loaded

