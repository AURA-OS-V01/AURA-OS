from governance.constitution.rules import AuraConstitution

def test_constitution():

    constitution = AuraConstitution()

    print("AURA Constitution Test")

    print("---------------------")

    for rule in constitution.get_rules():

        print(rule)

if __name__ == "__main__":

    test_constitution()