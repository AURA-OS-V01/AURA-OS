from agents.core.agent import Agent

class SecurityAgent(Agent):

    """

    AURA internal security specialist.

    """

    def __init__(self):

        super().__init__(

            "AURA Security Agent",

            "security_specialist"

        )

        self.permissions = [

            "audit_system",

            "report_vulnerabilities",

            "monitor_security"

        ]

        self.findings = []

    def report_issue(

        self,

        issue: str,

        severity: str

    ):

        finding = {

            "issue": issue,

            "severity": severity

        }

        self.findings.append(finding)

        return finding

    def get_findings(self):

        return self.findings