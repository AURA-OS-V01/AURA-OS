from kernel.events.event import Event

from kernel.events.event_bus import EventBus

class AuraRuntime:

    """

    Central runtime coordinator for AURA.

    """

    def __init__(self):

        self.event_bus = EventBus()

        self.agents = {}

        self.models = {}

        self.tools = {}

        self.memory = None

    def register_agent(self, agent):

        self.agents[agent.name] = agent

    def register_model(self, name, model):

        self.models[name] = model

    def register_tool(self, name, tool):

        self.tools[name] = tool

    def set_memory(self, memory):

        self.memory = memory

    def emit_event(self, event_type, source, data=None):

        event = Event(

            event_type,

            source,

            data

        )

        self.event_bus.publish(event)

    def status(self):

        return {

            "agents": list(self.agents.keys()),

            "models": list(self.models.keys()),

            "tools": list(self.tools.keys()),

            "memory_connected": self.memory is not None

        }