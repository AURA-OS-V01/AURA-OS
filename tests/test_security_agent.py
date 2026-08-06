from agents.security.security_agent import SecurityAgent

def test_security_agent():

    agent = SecurityAgent()

    result = agent.report_issue(

        "Unused permission detected",

        "MEDIUM"

    )

    print("Security Agent Test")

    print("-------------------")

    print(agent.describe())

    print(result)

if __name__ == "__main__":

    test_security_agent()