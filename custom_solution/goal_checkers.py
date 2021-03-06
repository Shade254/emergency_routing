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
        is_goal = node.get_node_id() == self.__goal_id
        if is_goal:
            self.__finished = True
        return is_goal

    def finish_search(self):
        return self.__finished


class ExitGoalChecker(GoalChecker):
    def __init__(self, graph):
        self.__finished = False
        self.__graph = graph

    def is_goal(self, node):
        is_goal = self.__graph.get_node(node.get_node_id()).is_exit
        if is_goal:
            self.__finished = True
        return is_goal

    def finish_search(self):
        return self.__finished
