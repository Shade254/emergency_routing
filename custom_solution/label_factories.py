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
                new_label = CostLabel(label, e.to_node, label.get_people(), cost + edge_cost)
                children.append(new_label)
        return children

    def get_start_labels(self, node_id, people):
        return [CostLabel(None, node_id, people, 0)]


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
                new_label = HeuristicCostLabel(label, next_node.name, label.get_people(), cost + edge_cost,
                                               self._heuristic.get_estimate(next_node))
                children.append(new_label)
        return children

    def get_start_labels(self, node_id, people):
        return [HeuristicCostLabel(None, node_id, people, 0, self._heuristic.get_estimate(self._graph.get_node(node_id)))]
