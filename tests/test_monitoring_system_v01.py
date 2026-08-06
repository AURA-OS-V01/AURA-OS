from core.operations.monitoring_system_v01 import (

    MonitoringSystem

)

def test_monitoring_system():

    monitor = MonitoringSystem()

    result = monitor.monitor(

        "Dashboard Build"

    )

    print("Monitoring System Test")

    print("----------------------")

    print(result)

if __name__ == "__main__":

    test_monitoring_system()