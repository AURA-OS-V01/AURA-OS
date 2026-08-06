from core.knowledge.graph.aura_knowledge_graph_engine_v01 import (

    AURAKnowledgeGraphEngine

)

def test_knowledge_graph():

    graph = AURAKnowledgeGraphEngine()

    ai = graph.add_node(

        "Artificial Intelligence"

    )

    agents = graph.add_node(

        "Agents"

    )

    graph.add_relationship(

        ai["id"],

        agents["id"],

        "contains"

    )

    related = graph.find_related(

        ai["id"]

    )

    assert len(graph.nodes) == 2

    assert len(related) == 1

if __name__ == "__main__":

    test_knowledge_graph()