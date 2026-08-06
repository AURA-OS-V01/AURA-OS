from core.growth.sales_agent_v01 import (

    AURASalesAgent

)

def test_sales_agent():

    agent = AURASalesAgent()

    lead = {

        "company":

            "Example Logistics",

        "industry":

            "Transportation",

        "score":

            90

    }

    result = agent.create_sales_strategy(

        lead,

        "Acquire as automation client"

    )

    print("AURA Sales Agent Test")

    print("---------------------")

    print(result)

if __name__ == "__main__":

    test_sales_agent()