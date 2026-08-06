class AdaptiveSelector:

    """

    Selects agents using capability

    and performance data.

    """

    def __init__(

        self,

        registry,

        performance

    ):

        self.registry = registry

        self.performance = performance

    def select(

        self,

        capability

    ):

        candidates = self.registry.find_agents(

            capability

        )

        if not candidates:

            return None

        ranked = []

        for agent in candidates:

            score = self.performance.get_score(

                agent["name"]

            )

            success_rate = 0

            if score:

                success_rate = score["success_rate"]

            ranked.append(

                {

                    "agent": agent,

                    "score": success_rate

                }

            )

        ranked.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return ranked[0]