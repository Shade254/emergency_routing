class GoalChecker:
    def is_goal(self, node):
        pass

    def finish_search(self):
        pass


class SingleNodeGoalChecker(GoalChecker):
    def __init__(self, goal_id):
        self.__finished = False
        self.__goal_id = goal_id

    def is_goal(self, node):
        is_goal = node.name == self.__goal_id
        if is_goal:
            self.__finished = True
        return is_goal

    def finish_search(self):
        return self.__finished
