class Heuristic:
    def __init__(self, graph, goal_checker):
        self.__graph = graph
        self.__goal_checker = goal_checker

    def get_estimate(self, node):
        pass


class ConstantHeuristic(Heuristic):
    def __init__(self, graph, goal_checker, value=0):
        super().__init__(graph, goal_checker)
        self.__graph = graph
        self.__goal_checker = goal_checker
        self.__value = value

    def get_estimate(self, node):
        if self.__goal_checker.is_goal(node):
            return 0
        else:
            return self.__value
