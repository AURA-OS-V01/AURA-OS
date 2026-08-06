from uuid import uuid4

from datetime import datetime

class AURAEnterpriseAgentMarketplace:

    def __init__(self):

        self.agent_templates = []

        self.deployed_agents = []

    def create_agent_template(

        self,

        name,

        category,

        capabilities

    ):

        template = {

            "id":

                str(uuid4()),

            "name":

                name,

            "category":

                category,

            "capabilities":

                capabilities,

            "created":

                datetime.utcnow().isoformat()

        }

        self.agent_templates.append(

            template

        )

        return template

    def find_agents(

        self,

        category

    ):

        return [

            agent

            for agent in self.agent_templates

            if agent["category"] == category

        ]

    def deploy_agent(

        self,

        template_id,

        business_id

    ):

        deployment = {

            "id":

                str(uuid4()),

            "template_id":

                template_id,

            "business_id":

                business_id,

            "status":

                "active",

            "created":

                datetime.utcnow().isoformat()

        }

        self.deployed_agents.append(

            deployment

        )

        return deployment

    def get_marketplace(self):

        return {

            "templates":

                self.agent_templates,

            "deployments":

                self.deployed_agents

        }