class ImprovementEngine:

    """

    Analyzes agent performance

    and suggests improvements.

    """

    def __init__(

        self,

        performance,

        memory

    ):

        self.performance = performance

        self.memory = memory

    def analyze(

        self,

        agent

    ):

        score = self.performance.get_score(

            agent

        )

        memories = self.memory.recall(

            agent

        )

        recommendation = "No changes needed"

        if score:

            if score["success_rate"] < 0.5:

                recommendation = (

                    "Review agent strategy"

                )

            elif score["success_rate"] < 0.8:

                recommendation = (

                    "Provide additional training"

                )

            else:

                recommendation = (

                    "Continue current strategy"

                )

        return {

            "agent": agent,

            "performance": score,

            "memories_reviewed": len(memories),

            "recommendation": recommendation

        }