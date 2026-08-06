from aura_platform.preferences.personalization_profile_v01 import (

    PersonalizationProfile

)

def test_personalization():

    profile_system = PersonalizationProfile()

    result = profile_system.create_profile(

        "user001",

        "English",

        "Advanced",

        "Research"

    )

    print("Personalization Profile Test")

    print("---------------------------")

    print(result)

if __name__ == "__main__":

    test_personalization()