from agents.marketing.marketing_agent import MarketingAgent

def test_marketing_agent():

    agent = MarketingAgent()

    result = agent.analyze_market(

        "AI automation services"

    )

    print("Marketing Agent Test")

    print("-------------------")

    print(agent.describe())

    print(result)

if __name__ == "__main__":

    test_marketing_agent()