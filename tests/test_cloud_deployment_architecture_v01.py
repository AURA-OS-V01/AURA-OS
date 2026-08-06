from core.deployment.cloud_deployment_architecture_v01 import (

    CloudDeploymentArchitecture

)

def test_cloud_architecture():

    system = CloudDeploymentArchitecture()

    result = system.create_environment(

        "Production",

        [

            "API Service",

            "Agent Service",

            "Memory Service",

            "Database Service"

        ],

        "ready"

    )

    print("Cloud Deployment Architecture Test")

    print("----------------------------------")

    print(result)

if __name__ == "__main__":

    test_cloud_architecture()