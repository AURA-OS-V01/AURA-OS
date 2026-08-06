from aura_platform.education.education_mode_v01 import (

    EducationMode

)

def test_education_mode():

    education = EducationMode()

    result = education.create_profile(

        "child",

        "Physics",

        "Beginner"

    )

    print("Education Mode Test")

    print("-------------------")

    print(result)

if __name__ == "__main__":

    test_education_mode()