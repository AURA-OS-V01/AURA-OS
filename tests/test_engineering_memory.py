from core.learning.engineering_memory import (

    EngineeringMemory

)

def test_engineering_memory():

    memory = EngineeringMemory()

    result = memory.store(

        "AURA Dashboard",

        "React + FastAPI",

        "success",

        "Good architecture for agent platforms"

    )

    print("Engineering Memory Test")

    print("----------------------")

    print(result)

if __name__ == "__main__":

    test_engineering_memory()