from agents.finance.finance_agent import FinanceAgent

def test_finance_agent():

    agent = FinanceAgent()

    result = agent.evaluate_opportunity(

        "AI automation service",

        "High",

        "Medium"

    )

    print("Finance Agent Test")

    print("-----------------")

    print(agent.describe())

    print(result)

if __name__ == "__main__":

    test_finance_agent()