from agents.product.deployment_planner_v01 import (

    DeploymentPlanner

)

def test_deployment_planner():

    planner = DeploymentPlanner()

    result = planner.create_plan(

        "Fitness App"

    )

    print("Deployment Planner Test")

    print("----------------------")

    print(result)

if __name__ == "__main__":

    test_deployment_planner()