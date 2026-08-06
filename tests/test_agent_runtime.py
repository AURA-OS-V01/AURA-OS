from agents.runtime.agent_runtime import AgentRuntime

def test_runtime():

    agent = AgentRuntime(

        "Research Agent",

        [

            "market_analysis",

            "trend_detection"

        ],

        [

            "read_workspace"

        ]

    )

    result = agent.execute(

        "Analyze AI market trends",

        "market_analysis"

    )

    denied = agent.execute(

        "Deploy system",

        "system_change"

    )

    print("Agent Runtime Test")

    print("------------------")

    print(result)

    print(denied)

if __name__ == "__main__":

    test_runtime()