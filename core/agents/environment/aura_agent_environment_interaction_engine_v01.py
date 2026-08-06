from uuid import uuid4

from datetime import datetime

class AURAAgentEnvironmentInteractionEngine:

    def __init__(self):

        self.environments = []

        self.observations = []

        self.actions = []

    def create_environment(

        self,

        name,

        description

    ):

        environment = {

            "id":

                str(uuid4()),

            "name":

                name,

            "description":

                description,

            "state":

                {},

            "created":

                datetime.utcnow().isoformat()

        }

        self.environments.append(

            environment

        )

        return environment

    def update_state(

        self,

        environment_id,

        key,

        value

    ):

        for environment in self.environments:

            if environment["id"] == environment_id:

                environment["state"][key] = value

                return environment

        return None

    def observe(

        self,

        agent_id,

        environment_id

    ):

        for environment in self.environments:

            if environment["id"] == environment_id:

                observation = {

                    "id":

                        str(uuid4()),

                    "agent_id":

                        agent_id,

                    "environment_id":

                        environment_id,

                    "state":

                        environment["state"],

                    "created":

                        datetime.utcnow().isoformat()

                }

                self.observations.append(

                    observation

                )

                return observation

        return None

    def record_action(

        self,

        agent_id,

        environment_id,

        action

    ):

        action_record = {

            "id":

                str(uuid4()),

            "agent_id":

                agent_id,

            "environment_id":

                environment_id,

            "action":

                action,

            "created":

                datetime.utcnow().isoformat()

        }

        self.actions.append(

            action_record

        )

        return action_record

    def get_observations(self):

        return self.observations

    def get_actions(self):

        return self.actions