class Heuristic:
    def __init__(self, graph):
        self._graph = graph

    def get_estimate(self, node):
        pass


class ConstantHeuristic(Heuristic):
    def __init__(self, graph, goal_ids, value=0):
        super().__init__(graph)
        self.__value = value
        self.__goal_ids = goal_ids

    def get_estimate(self, node):
        if node.name in self.__goal_ids:
            return 0
        else:
            return self.__value
