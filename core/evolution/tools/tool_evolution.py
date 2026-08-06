class ToolEvolutionEngine:

    """

    Evaluates tools and recommends

    improvements.

    """

    def __init__(self):

        self.reviews = []

    def analyze(

        self,

        tool_name,

        success_rate,

        usage_count

    ):

        recommendation = (

            "Tool performing well"

        )

        if success_rate < 0.5:

            recommendation = (

                "Replace or redesign tool"

            )

        elif success_rate < 0.8:

            recommendation = (

                "Improve tool reliability"

            )

        result = {

            "tool": tool_name,

            "usage": usage_count,

            "success_rate": success_rate,

            "recommendation": recommendation

        }

        self.reviews.append(result)

        return result