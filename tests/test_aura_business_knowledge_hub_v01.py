from core.business.knowledge.aura_business_knowledge_hub_v01 import (

    AURABusinessKnowledgeHub

)

def test_business_knowledge_hub():

    hub = AURABusinessKnowledgeHub()

    knowledge = hub.add_knowledge(

        "aura_company",

        "Product Information",

        "product",

        "AI automation platform for businesses"

    )

    results = hub.search_knowledge(

        "aura_company",

        "product"

    )

    all_data = hub.get_business_knowledge(

        "aura_company"

    )

    print(

        "AURA Business Knowledge Hub Test"

    )

    print(

        "--------------------------------"

    )

    print(all_data)

    assert knowledge["category"] == (

        "product"

    )

    assert len(results) == 1

    assert len(all_data) == 1

if __name__ == "__main__":

    test_business_knowledge_hub()