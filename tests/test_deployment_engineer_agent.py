from agents.builders.deployment.deployment_engineer_agent import (

    DeploymentEngineerAgent

)

def test_deployment_engineer():

    agent = DeploymentEngineerAgent()

    result = agent.create_plan(

        "AURA Dashboard",

        {

            "frontend": "React",

            "backend": "FastAPI",

            "database": "PostgreSQL"

        }

    )

    print("Deployment Engineer Agent Test")

    print("------------------------------")

    print(result)

if __name__ == "__main__":

    test_deployment_engineer()