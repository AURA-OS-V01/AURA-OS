from core.memory.experience_memory_system_v01 import (

    ExperienceMemorySystem

)

def test_experience_memory():

    memory = ExperienceMemorySystem()

    result = memory.record(

        "Education Platform",

        "Successful",

        "Age based explanations improved learning"

    )

    print("Experience Memory Test")

    print("---------------------")

    print(result)

if __name__ == "__main__":

    test_experience_memory()