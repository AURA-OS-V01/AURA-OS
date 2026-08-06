from core.routing.agent_router import AgentRouter

def test_router():

    router = AgentRouter()

    result = router.route(

        "Analyze a new business opportunity"

    )

    print("Agent Router Test")

    print("-----------------")

    print(result)

if __name__ == "__main__":

    test_router()