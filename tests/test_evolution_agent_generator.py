from core.evolution.agents.evolution_agent_generator import (

    EvolutionAgentGenerator

)

def test_evolution_generator():

    generator = EvolutionAgentGenerator()

    result = generator.generate(

        "legal_analysis",

        "Repeated compliance tasks require a specialist"

    )

    proposals = generator.list_proposals()

    print("Evolution Agent Generator Test")

    print("-----------------------------")

    print(result)

    print(proposals)

if __name__ == "__main__":

    test_evolution_generator()