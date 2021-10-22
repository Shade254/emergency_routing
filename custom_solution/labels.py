class Label:
    def __init__(self, predecessor, node):
        self.__predecessor = predecessor
        self.__node = node

    def get_cost(self):
        pass

    def get_node(self):
        return self.__node

    def get_predecessor(self):
        return self.__predecessor


class PeopleLabel(Label):
    def __init__(self, predecessor, node, people):
        super().__init__(predecessor, node)
        self.__people = people

    def get_people(self):
        return self.__people


class CostLabel(PeopleLabel):
    def __init__(self, predecessor, node, people, cost):
        super().__init__(predecessor, node, people)
        self.__cost = cost

    def get_cost(self):
        return self.__cost


class HeuristicCostLabel(CostLabel):
    def __init__(self, predecessor, node, people, cost, heuristic_estimate):
        super().__init__(predecessor, node, people, cost)
        self.__estimate = heuristic_estimate

    def get_cost(self):
        return self.__cost + self.__estimate

    def get_cost_only(self):
        return self.__cost

    def get_heuristic_only(self):
        return self.__estimate
