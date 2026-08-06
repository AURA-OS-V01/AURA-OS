from agents.research.research_agent import ResearchAgent

def test_research_agent():

    agent = ResearchAgent()

    result = agent.add_finding(

        "AI automation",

        "Businesses are looking for ways to reduce manual work."

    )

    print("Research Agent Test")

    print("------------------")

    print(agent.describe())

    print(result)

if __name__ == "__main__":

    test_research_agent()