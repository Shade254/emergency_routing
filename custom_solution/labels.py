class Label:
    def __init__(self, predecessor, node_id):
        self._predecessor = predecessor
        self._node_id = node_id

    def get_cost(self):
        pass

    def get_node_id(self):
        return self._node_id

    def get_predecessor(self):
        return self._predecessor

    def __str__(self):
        predcessor = "None"
        if self.get_predecessor():
            predcessor = self.get_predecessor().get_node_id()
        return "{Node: %s, Cost: %s, Predcessor: %s}" % (self.get_node_id(), self.get_cost(), predcessor)

    def __eq__(self, other):
        return self._node_id == other.get_node_id() and self.get_cost() == other.get_cost() and self._predecessor == other.get_predecessor()

    def __lt__(self, other):
        if self.get_cost() == other.get_cost():
            if self.get_node_id() == other.get_node_id():
                return self.get_predecessor().get_node_id() < other.get_predecessor().get_node_id()
            else:
                return self.get_node_id() < other.get_node_id()
        else:
            return self.get_cost() < other.get_cost()


class PeopleLabel(Label):
    def __init__(self, predecessor, node_id, people):
        super().__init__(predecessor, node_id)
        self._people = people

    def get_people(self):
        return self._people


class CostLabel(PeopleLabel):
    def __init__(self, predecessor, node_id, people, cost):
        super().__init__(predecessor, node_id, people)
        self._cost = cost

    def get_cost(self):
        return self._cost


class HeuristicCostLabel(CostLabel):
    def __init__(self, predecessor, node_id, people, cost, heuristic_estimate):
        super().__init__(predecessor, node_id, people, cost)
        self._estimate = heuristic_estimate

    def get_cost(self):
        return self._cost + self._estimate

    def get_cost_only(self):
        return self._cost

    def get_heuristic_only(self):
        return self._estimate
