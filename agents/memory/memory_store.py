import json

import os

from datetime import datetime

from uuid import uuid4

class MemoryStore:

    """

    Persistent memory storage

    for AURA agents.

    """

    def __init__(

        self,

        file_path="agent_memory.json"

    ):

        self.file_path = file_path

        if os.path.exists(

            self.file_path

        ):

            with open(

                self.file_path,

                "r"

            ) as file:

                self.memories = json.load(file)

        else:

            self.memories = []

    def store(

        self,

        agent,

        information

    ):

        memory = {

            "id": str(uuid4()),

            "agent": agent,

            "information": information,

            "created": datetime.utcnow().isoformat()

        }

        self.memories.append(

            memory

        )

        self.save()

        return memory

    def save(self):

        with open(

            self.file_path,

            "w"

        ) as file:

            json.dump(

                self.memories,

                file,

                indent=4

            )

    def recall(

        self,

        agent

    ):

        return [

            memory

            for memory in self.memories

            if memory["agent"] == agent

        ]