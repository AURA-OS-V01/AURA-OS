from uuid import uuid4

from datetime import datetime

class AURAWorldModelEnvironmentLayer:

    def __init__(self):

        self.entities = []

        self.signals = []

        self.context = []

    def add_entity(

        self,

        name,

        entity_type,

        description

    ):

        entity = {

            "id":

                str(uuid4()),

            "name":

                name,

            "type":

                entity_type,

            "description":

                description,

            "created":

                datetime.utcnow().isoformat()

        }

        self.entities.append(

            entity

        )

        return entity

    def record_signal(

        self,

        source,

        signal_type,

        value

    ):

        signal = {

            "id":

                str(uuid4()),

            "source":

                source,

            "type":

                signal_type,

            "value":

                value,

            "created":

                datetime.utcnow().isoformat()

        }

        self.signals.append(

            signal

        )

        return signal

    def update_context(

        self,

        key,

        value

    ):

        context_item = {

            "id":

                str(uuid4()),

            "key":

                key,

            "value":

                value,

            "created":

                datetime.utcnow().isoformat()

        }

        self.context.append(

            context_item

        )

        return context_item

    def get_world_state(self):

        return {

            "entities":

                self.entities,

            "signals":

                self.signals,

            "context":

                self.context

        }