from core.security.system_reliability_monitoring_v01 import (

    SystemReliabilityMonitoring

)

def test_reliability_monitoring():

    system = SystemReliabilityMonitoring()

    result = system.record_health(

        "Agent Communication System",

        "Healthy",

        "Operating normally"

    )

    print("System Reliability Monitoring Test")

    print("----------------------------------")

    print(result)

if __name__ == "__main__":

    test_reliability_monitoring()