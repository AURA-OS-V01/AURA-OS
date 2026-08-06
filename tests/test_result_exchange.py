from agents.results.result_exchange import ResultExchange

def test_results():

    exchange = ResultExchange()

    result = exchange.submit_result(

        "Research Agent",

        "Market analysis",

        {

            "market": "AI automation",

            "growth": "strong"

        },

        0.85

    )

    print("Result Exchange Test")

    print("-------------------")

    print(result)

if __name__ == "__main__":

    test_results()