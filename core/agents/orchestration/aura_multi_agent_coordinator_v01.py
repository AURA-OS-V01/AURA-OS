from uuid import uuid4

from datetime import datetime

class AURAMultiAgentCoordinator:

    def __init__(self):

        self.agents = []

        self.teams = []

        self.assignments = []

    def register_agent(

        self,

        name,

        role

    ):

        agent = {

            "id":

                str(uuid4()),

            "name":

                name,

            "role":

                role,

            "status":

                "available",

            "created":

                datetime.utcnow().isoformat()

        }

        self.agents.append(agent)

        return agent

    def create_team(

        self,

        name,

        agent_ids

    ):

        team = {

            "id":

                str(uuid4()),

            "name":

                name,

            "agents":

                agent_ids,

            "created":

                datetime.utcnow().isoformat()

        }

        self.teams.append(team)

        return team

    def delegate_task(

        self,

        team_id,

        task

    ):

        assignment = {

            "id":

                str(uuid4()),

            "team_id":

                team_id,

            "task":

                task,

            "status":

                "assigned",

            "created":

                datetime.utcnow().isoformat()

        }

        self.assignments.append(

            assignment

        )

        return assignment

    def get_team_agents(

        self,

        team_id

    ):

        for team in self.teams:

            if team["id"] == team_id:

                return [

                    agent

                    for agent in self.agents

                    if agent["id"] in team["agents"]

                ]

        return []

    def get_assignments(self):

        return self.assignments