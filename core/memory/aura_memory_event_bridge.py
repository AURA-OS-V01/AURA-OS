
class AURAMemoryEventBridge:

    def __init__(

        self,

        event_bus,

        memory

    ):

        self.event_bus = event_bus

        self.memory = memory

    def record_execution(

        self,

        execution

    ):

        memory_record = self.memory.remember(

            execution

        )

        event = self.event_bus.publish(

            "agent.execution.completed",

            memory_record

        )

        return {

            "memory": memory_record,

            "event": event

        }

