class WorkflowOptimizer:

    """

    Analyzes workflows and suggests improvements.

    """

    def __init__(self):

        self.optimizations = []

    def analyze(

        self,

        workflow

    ):

        recommendation = (

            "Workflow is already optimized"

        )

        if len(workflow) > 3:

            recommendation = (

                "Consider parallel execution"

            )

        result = {

            "workflow": workflow,

            "recommendation": recommendation

        }

        self.optimizations.append(result)

        return result