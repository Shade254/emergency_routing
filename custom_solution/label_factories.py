from custom_solution.collisions import NegativeConstraint
from labels import *


class LabelFactory:
    def __init__(self, graph):
        self._graph = graph

    def expand(self, label):
        pass

    def get_start_labels(self, node_name, people):
        pass


class CostLabelFactory(LabelFactory):
    def __init__(self, graph, cost_function):
        super().__init__(graph)
        self._cost_function = cost_function

    def expand(self, label):
        cost = label.get_cost()
        children = []
        for e in self._graph.get_out_edges(label.get_node_id()):
            edge_cost = self._cost_function.get_risk(label.get_people(), e)
            if edge_cost:
                new_label = CostLabel(label, e.to_node, label.get_people(), label.get_travel_time() + e.travel_time,
                                      cost + edge_cost)
                children.append(new_label)
        return children

    def get_start_labels(self, node_id, people):
        return [CostLabel(None, node_id, people, 0, 0)]


class ConstrainedCostLabelFactory(CostLabelFactory):
    def __init__(self, graph, cost_function, constraints):
        super().__init__(graph, cost_function)
        self.negative_constraints = {}
        self.positive_constraints = {}
        for c in constraints:
            if isinstance(c, NegativeConstraint):
                if c.when not in self.negative_constraints:
                    self.negative_constraints[c.when] = []
                self.negative_constraints[c.when].append(c)
            else:
                if c.when not in self.positive_constraints:
                    self.positive_constraints[c.when] = []
                self.positive_constraints[c.when].append(c)

    def expand(self, label):
        cost = label.get_cost()
        children = []
        time = label.get_travel_time()

        negative_constraints = []
        positive_constraints = []
        if time in self.negative_constraints:
            negative_constraints = self.negative_constraints[time]
        elif time in self.negative_constraints:
            positive_constraints = self.positive_constraints[time]

        for e in self._graph.get_out_edges(label.get_node_id()):
            add = True
            for c in negative_constraints:
                if c.edge == e:
                    add = False
                    break
            for c in positive_constraints:
                if c.edge != e:
                    add = False
                    break

            if not add:
                print("Negative Applied constrained " + str(label) + "  --  " + str(e))
                continue

            edge_cost = self._cost_function.get_risk(label.get_people(), e)
            if edge_cost:
                new_label = CostLabel(label, e.to_node, label.get_people(), label.get_travel_time() + e.travel_time,
                                      cost + edge_cost)
                children.append(new_label)
        return children


class HeuristicCostLabelFactory(CostLabelFactory):
    def __init__(self, graph, cost_function, heuristic):
        super().__init__(graph, cost_function)
        self._heuristic = heuristic

    def expand(self, label):
        cost = label.get_cost_only()
        children = []
        for e in self._graph.get_out_edges(label.get_node_id()):
            next_node = self._graph.get_node(e.to_node)
            edge_cost = self._cost_function.get_risk(label.get_people(), e)
            if edge_cost:
                new_label = HeuristicCostLabel(label, next_node.name, label.get_people(),
                                               label.get_travel_time() + e.travel_time, cost + edge_cost,
                                               self._heuristic.get_estimate(next_node))
                children.append(new_label)
        return children

    def get_start_labels(self, node_id, people):
        return [HeuristicCostLabel(None, node_id, people, 0, 0,
                                   self._heuristic.get_estimate(self._graph.get_node(node_id)))]
