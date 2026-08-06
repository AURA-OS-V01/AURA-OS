from core.security.data_privacy_controls_v01 import (

    DataPrivacyControls

)

def test_privacy_controls():

    system = DataPrivacyControls()

    result = system.create_privacy_profile(

        "user001",

        True,

        False,

        "limited"

    )

    print("Data Privacy Controls Test")

    print("--------------------------")

    print(result)

if __name__ == "__main__":

    test_privacy_controls()