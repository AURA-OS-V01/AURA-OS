from uuid import uuid4

from datetime import datetime

class AURAAgentKnowledgeIntegrationEngine:

    def __init__(self):

        self.knowledge_items = []

        self.access_logs = []

    def add_knowledge(

        self,

        topic,

        information,

        source

    ):

        knowledge = {

            "id":

                str(uuid4()),

            "topic":

                topic,

            "information":

                information,

            "source":

                source,

            "created":

                datetime.utcnow().isoformat()

        }

        self.knowledge_items.append(

            knowledge

        )

        return knowledge

    def query_knowledge(

        self,

        agent_id,

        keyword

    ):

        results = [

            item

            for item in self.knowledge_items

            if keyword.lower()

            in item["topic"].lower()

        ]

        self.access_logs.append({

            "agent_id":

                agent_id,

            "query":

                keyword,

            "results":

                len(results),

            "created":

                datetime.utcnow().isoformat()

        })

        return results

    def get_agent_context(

        self,

        agent_id,

        topic

    ):

        knowledge = self.query_knowledge(

            agent_id,

            topic

        )

        return {

            "agent_id":

                agent_id,

            "context":

                knowledge

        }

    def get_access_logs(self):

        return self.access_logs