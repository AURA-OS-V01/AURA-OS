
class AURALearningBridge:

    def __init__(

        self,

        memory,

        learning

    ):

        self.memory = memory

        self.learning = learning

    def process(

        self,

        execution

    ):

        record = self.memory.remember(

            execution

        )

        lesson = self.learning.learn(

            execution

        )

        return {

            "memory": record,

            "lesson": lesson

        }

