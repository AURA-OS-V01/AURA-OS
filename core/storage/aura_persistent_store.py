
import json

from pathlib import Path

from datetime import datetime, UTC

class AURAPersistentStore:

    def __init__(self, path="aura_state.json"):

        self.path = Path(path)

        self.state = self.load()

    def load(self):

        if self.path.exists():

            with open(self.path, "r") as f:

                return json.load(f)

        return {

            "missions": [],

            "agents": [],

            "events": [],

            "lessons": [],

            "created": datetime.now(

                UTC

            ).isoformat()

        }

    def save(self):

        with open(self.path, "w") as f:

            json.dump(

                self.state,

                f,

                indent=4

            )

    def add(

        self,

        category,

        data

    ):

        if category not in self.state:

            self.state[category] = []

        self.state[category].append(

            data

        )

        self.save()

        return data

    def get(self, category):

        return self.state.get(

            category,

            []

        )

    def status(self):

        return {

            key: len(value)

            if isinstance(value, list)

            else value

            for key, value in self.state.items()

        }

