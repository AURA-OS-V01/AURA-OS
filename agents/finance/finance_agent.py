from agents.core.agent import Agent

class FinanceAgent(Agent):

    """

    AURA finance and business analysis specialist.

    """

    def __init__(self):

        super().__init__(

            "AURA Finance Agent",

            "finance_specialist"

        )

        self.permissions = [

            "analyze_costs",

            "evaluate_opportunities",

            "track_financial_metrics"

        ]

        self.analysis = []

    def evaluate_opportunity(

        self,

        opportunity: str,

        potential: str,

        risk: str

    ):

        result = {

            "opportunity": opportunity,

            "potential": potential,

            "risk": risk

        }

        self.analysis.append(result)

        return result

    def get_analysis(self):

        return self.analysis