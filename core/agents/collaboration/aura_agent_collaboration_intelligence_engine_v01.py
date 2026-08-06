from uuid import uuid4

from datetime import datetime

class AURAAgentCollaborationIntelligenceEngine:

    def __init__(self):

        self.collaborations = []

        self.team_reports = []

    def record_collaboration(

        self,

        agents,

        task,

        success,

        score

    ):

        collaboration = {

            "id":

                str(uuid4()),

            "agents":

                agents,

            "task":

                task,

            "success":

                success,

            "score":

                score,

            "created":

                datetime.utcnow().isoformat()

        }

        self.collaborations.append(

            collaboration

        )

        return collaboration

    def analyze_team(

        self,

        agents

    ):

        records = [

            record

            for record in self.collaborations

            if set(record["agents"]) ==

               set(agents)

        ]

        if not records:

            return None

        average_score = (

            sum(

                record["score"]

                for record in records

            )

            /

            len(records)

        )

        success_rate = (

            sum(

                1

                for record in records

                if record["success"]

            )

            /

            len(records)

        )

        report = {

            "agents":

                agents,

            "average_score":

                average_score,

            "success_rate":

                success_rate,

            "collaborations":

                len(records)

        }

        self.team_reports.append(

            report

        )

        return report

    def suggest_team_improvement(

        self,

        agents

    ):

        report = self.analyze_team(

            agents

        )

        if not report:

            return None

        if report["average_score"] < 70:

            return "Improve agent coordination"

        else:

            return "Team performance is optimal"

    def get_reports(self):

        return self.team_reports