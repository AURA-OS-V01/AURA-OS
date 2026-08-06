from core.optimization.workflow_optimizer import WorkflowOptimizer

def test_optimizer():

    optimizer = WorkflowOptimizer()

    result = optimizer.analyze(

        [

            "Research",

            "Finance",

            "Security",

            "Report"

        ]

    )

    print("Workflow Optimizer Test")

    print("----------------------")

    print(result)

if __name__ == "__main__":

    test_optimizer()