from core.memory.knowledge_base_system_v01 import (

    KnowledgeBaseSystem

)

def test_knowledge_base():

    system = KnowledgeBaseSystem()

    result = system.store(

        "Education mode adapts by age range",

        "Product Design"

    )

    print("Knowledge Base Test")

    print("-------------------")

    print(result)

if __name__ == "__main__":

    test_knowledge_base()