from datetime import datetime

from uuid import uuid4

class AURAKnowledgeGraphEngine:

    def __init__(self):

        self.nodes = []

        self.edges = []

    def add_node(

        self,

        name,

        node_type="concept"

    ):

        node = {

            "id": str(uuid4()),

            "name": name,

            "type": node_type,

            "created": datetime.utcnow().isoformat()

        }

        self.nodes.append(

            node

        )

        return node

    def add_relationship(

        self,

        source_id,

        target_id,

        relationship

    ):

        edge = {

            "id": str(uuid4()),

            "source": source_id,

            "target": target_id,

            "relationship": relationship

        }

        self.edges.append(

            edge

        )

        return edge

    def find_related(

        self,

        node_id

    ):

        results = []

        for edge in self.edges:

            if edge["source"] == node_id:

                results.append(edge)

            if edge["target"] == node_id:

                results.append(edge)

        return results

    def get_state(

        self

    ):

        return {

            "nodes": self.nodes,

            "edges": self.edges

        }