from agents.core.agent import Agent

class ResearchAgent(Agent):

    """

    AURA research and discovery specialist.

    """

    def __init__(self):

        super().__init__(

            "AURA Research Agent",

            "research_specialist"

        )

        self.permissions = [

            "collect_information",

            "analyze_trends",

            "study_opportunities"

        ]

        self.findings = []

    def add_finding(

        self,

        topic: str,

        insight: str

    ):

        finding = {

            "topic": topic,

            "insight": insight

        }

        self.findings.append(finding)

        return finding

    def get_findings(self):

        return self.findings