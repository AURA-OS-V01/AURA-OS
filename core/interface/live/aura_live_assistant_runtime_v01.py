from datetime import datetime

from uuid import uuid4

from core.runtime.aura_unified_intelligence_runtime_v01 import (

    AURAUnifiedIntelligenceRuntime,

)

from core.memory.aura_context_memory_engine_v01 import (

    AURAContextMemoryEngine,

)

class AURALiveAssistantRuntime:

    def __init__(self):

        self.session_id = str(uuid4())

        self.history = []

        self.runtime = AURAUnifiedIntelligenceRuntime()

        self.memory = AURAContextMemoryEngine()

    def process_input(

        self,

        message

    ):

        # Store incoming context

        self.memory.store_memory(

            message,

            "conversation"

        )

        # Retrieve related context

        context = self.memory.retrieve_memory(

            message.split()[0]

            if message.split()

            else None

        )

        execution = self.runtime.execute_request(

            message

        )

        response = self.generate_response(

            message,

            execution,

            context

        )

        entry = {

            "session": self.session_id,

            "message": message,

            "response": response,

            "execution": execution,

            "memory_context": context,

            "created": datetime.utcnow().isoformat()

        }

        self.history.append(

            entry

        )

        return response

    def generate_response(

        self,

        message,

        execution=None,

        context=None

    ):

        text = message.lower()

        if "research" in text:

            return "AURA stored the context and routed this through research capability."

        if "strategy" in text:

            return "AURA stored the context and routed this through strategy capability."

        if "build" in text:

            return "AURA created a build workflow with remembered context."

        return "AURA processed your request with contextual memory."

    def get_session_state(

        self

    ):

        return {

            "session_id": self.session_id,

            "history": self.history,

            "memory": self.memory.get_state(),

            "runtime": self.runtime.get_runtime_state()

        }

def start_aura_session():

    aura = AURALiveAssistantRuntime()

    print("AURA Live Assistant")

    print("Type 'exit' to close session.")

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() == "exit":

            break

        response = aura.process_input(

            user_input

        )

        print("\nAURA:", response)