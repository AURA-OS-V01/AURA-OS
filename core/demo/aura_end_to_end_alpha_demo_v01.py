from datetime import datetime

from uuid import uuid4

from core.interface.live.aura_live_assistant_runtime_v01 import (

    AURALiveAssistantRuntime,

)

class AURAEndToEndAlphaDemo:

    def __init__(self):

        self.session_id = str(uuid4())

        self.assistant = AURALiveAssistantRuntime()

        self.sessions = []

    def run_demo(

        self,

        user,

        mode,

        request

    ):

        response = self.assistant.process_input(

            request

        )

        session = {

            "id": self.session_id,

            "user": user,

            "mode": mode,

            "request": request,

            "response": response,

            "status": "completed",

            "created": datetime.utcnow().isoformat()

        }

        self.sessions.append(

            session

        )

        return session

    def get_state(

        self

    ):

        return {

            "sessions": self.sessions,

            "assistant": self.assistant.get_session_state()

        }

def run():

    aura = AURAEndToEndAlphaDemo()

    result = aura.run_demo(

        "Demo User",

        "autonomous",

        "Build an enterprise automation platform"

    )

    print("AURA END TO END DEMO")

    print("--------------------")

    print(result)

if __name__ == "__main__":

    run()