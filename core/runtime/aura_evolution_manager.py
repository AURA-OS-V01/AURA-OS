
from core.storage.aura_persistent_store import AURAPersistentStore

from core.learning.aura_learning_engine import (

    AURALearningEngine

)

from core.evolution.aura_self_improvement_loop import (

    AURASelfImprovementLoop

)

class AURAEvolutionManager:

    def __init__(self):
        self.storage = AURAPersistentStore()

        self.learning = AURALearningEngine()

        self.improvement = (

            AURASelfImprovementLoop(

                self.learning

            )

        )

    def record_execution(

        self,

        execution

    ):

        return self.learning.learn(

            execution

        )

    def analyze(self):

        result = self.improvement.analyze()

        self.storage.add(

            "improvements",

            result

        )

        return result

    def status(self):

        return {

            "lessons": self.learning.count(),

            "improvements": len(

                self.improvement.history()

            )

        }

