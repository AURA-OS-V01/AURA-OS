class AURAGoalManager:

    def __init__(self):

        self.goals = []

        self.counter = 1

    def create_goal(self, name, description, priority):

        goal = {

            "id": self.counter,

            "name": name,

            "description": description,

            "priority": priority,

            "status": "created"

        }

        self.counter += 1

        self.goals.append(goal)

        return goal.copy()

    def activate_goal(self, goal_id):

        for goal in self.goals:

            if goal["id"] == goal_id:

                goal["status"] = "active"

                return goal.copy()

        return None

    def complete_goal(self, goal_id):

        for goal in self.goals:

            if goal["id"] == goal_id:

                goal["status"] = "completed"

                return goal.copy()

        return None

    def get_goals(self):

        return [goal.copy() for goal in self.goals]

    def get_state(self):

        return {

            "goals": [goal.copy() for goal in self.goals],

            "count": len(self.goals),

            "total_goals": len(self.goals)

        }
