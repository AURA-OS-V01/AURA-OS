from uuid import uuid4

from datetime import datetime

class AURAGoalManagementPlanningEngine:

    def __init__(self):

        self.goals = []

        self.milestones = []

    def create_goal(

        self,

        title,

        description,

        priority

    ):

        goal = {

            "id":

                str(uuid4()),

            "title":

                title,

            "description":

                description,

            "priority":

                priority,

            "status":

                "active",

            "progress":

                0,

            "created":

                datetime.utcnow().isoformat()

        }

        self.goals.append(

            goal

        )

        return goal

    def add_milestone(

        self,

        goal_id,

        milestone

    ):

        milestone_record = {

            "id":

                str(uuid4()),

            "goal_id":

                goal_id,

            "milestone":

                milestone,

            "completed":

                False,

            "created":

                datetime.utcnow().isoformat()

        }

        self.milestones.append(

            milestone_record

        )

        return milestone_record

    def update_progress(

        self,

        goal_id,

        progress

    ):

        for goal in self.goals:

            if goal["id"] == goal_id:

                goal["progress"] = progress

                if progress >= 100:

                    goal["status"] = "completed"

                return goal

        return None

    def get_planning_state(self):

        return {

            "goals":

                self.goals,

            "milestones":

                self.milestones

        }