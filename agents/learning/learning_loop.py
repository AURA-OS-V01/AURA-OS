class LearningLoop:

    """

    Allows agents to learn

    from completed tasks.

    """

    def __init__(

        self,

        memory,

        performance

    ):

        self.memory = memory

        self.performance = performance

    def learn(

        self,

        agent,

        task,

        success,

        lesson

    ):

        self.performance.record_result(

            agent,

            success

        )

        self.memory.store(

            agent,

            {

                "task": task,

                "lesson": lesson,

                "success": success

            }

        )

        return {

            "agent": agent,

            "learned": True,

            "lesson": lesson

        }