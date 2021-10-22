from labels import *


class LabelFactory:
    def __init__(self, graph):
        self.__graph = graph

    def expand(self, label):
        pass

    def get_start_labels(self, node, people):
        pass


class CostLabelFactory(LabelFactory):
    def __init__(self, graph, cost_function):
        super().__init__(graph)
        self.__cost_function = cost_function

    def expand(self, label):
        cost = label.get_cost()
        children = []
        for e in self.__graph.get_out_edges(label.get_node()):
            next_node = self.__graph.get_node(e.to_node)
            new_label = CostLabel(label, next_node, label.get_people(), cost + self.__cost_function.get_risk(label.get_people(), e))
            children.append(new_label)
        return children

    def get_start_labels(self, node, people):
        first_label = CostLabel(None, node, people, 0)
        children = []
        for e in self.__graph.get_out_edges(node):
            next_node = self.__graph.get_node(e.to_node)
            new_label = CostLabel(first_label, next_node, people, self.__cost_function.get_risk(people, e))
            children.append(new_label)
        return children


class HeuristicCostLabelFactory(LabelFactory):
    def __init__(self, graph, cost_function, heuristic):
        super().__init__(graph)
        self.__cost_function = cost_function
        self.__heuristic = heuristic

    def expand(self, label):
        cost = label.get_cost()
        children = []
        for e in self.__graph.get_out_edges(label.get_node()):
            next_node = self.__graph.get_node(e.to_node)
            new_label = HeuristicCostLabel(label, next_node, label.get_people(), cost + self.__cost_function.get_risk(label.get_people(), e),
                                           self.__heuristic.get_estimate(next_node))
            children.append(new_label)
        return children

    def get_start_labels(self, node, people):
        first_label = HeuristicCostLabel(None, node, people, 0, self.__heuristic.get_estimate(node))
        children = []
        for e in self.__graph.get_out_edges(node):
            next_node = self.__graph.get_node(e.to_node)
            new_label = HeuristicCostLabel(first_label, next_node, people, self.__cost_function.get_risk(people, e), self.__heuristic.get_estimate(next_node))
            children.append(new_label)
        return children
