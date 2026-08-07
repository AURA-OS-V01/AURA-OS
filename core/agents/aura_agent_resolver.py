
class AURAAgentResolver:

    def __init__(self, lifecycle):

        self.lifecycle = lifecycle

    def resolve(self, name):

        agents = self.lifecycle.agents

        if name in agents:

            return agents[name]

        for agent_name, agent in agents.items():

            if name.lower() in agent_name.lower():

                return agent

        return None

