from paths import *
from label_factories import *
from goal_checkers import *
from heuristics import *
from queue import PriorityQueue


class SearchAlgorithm:
    def __init__(self, start_labels, label_factory, goal_checker):
        self.__label_factory = label_factory
        self.__goal_checker = goal_checker
        self._queue = PriorityQueue()
        self._closed_set = []
        for label in start_labels:
            self._add_to_queue(label)
            self._closed_set.append(label.get_node_id())

    def _add_to_queue(self, label):
        pass

    def _reconstruct_paths(self, end_labels):
        if not end_labels:
            print("No solution found")
            return end_labels
        else:
            paths = []
            for label in end_labels:
                paths.append(SimplePath(label))
            return paths

    def search(self):
        end_labels = []
        while not self._queue.empty():
            priority, current_label = self._queue.get()
            print("Picked " + current_label.__str__())

            if self.__goal_checker.is_goal(current_label):
                print("Is goal")
                end_labels.append(current_label)

            if self.__goal_checker.finish_search():
                print("Search finished")
                break

            children = self.__label_factory.expand(current_label)
            print("Number of children: %d" % len(children))
            for label in children:
                self._add_to_queue(label)
            self._closed_set.append(current_label.get_node_id())

        return self._reconstruct_paths(end_labels)


class SimpleDijkstra(SearchAlgorithm):
    def __init__(self, start_node_name, people, end_node_name, graph, cost_function):
        goal_checker = SingleNodeGoalChecker(end_node_name)
        label_factory = CostLabelFactory(graph, cost_function)
        start_labels = label_factory.get_start_labels(start_node_name, people)
        super().__init__(start_labels, label_factory, goal_checker)

    def _add_to_queue(self, label):
        if label.get_node_id() not in self._closed_set:
            print("Added " + label.__str__())
            self._queue.put((label.get_cost(), label))


class SimpleAStar(SearchAlgorithm):
    def __init__(self, start_node_name, people, end_node_name, graph, cost_function, heuristic=None):
        goal_checker = SingleNodeGoalChecker(end_node_name)
        if not heuristic:
            heuristic = ConstantHeuristic(graph, [end_node_name], 1)
        label_factory = HeuristicCostLabelFactory(graph, cost_function, heuristic)
        start_labels = label_factory.get_start_labels(start_node_name, people)
        super().__init__(start_labels, label_factory, goal_checker)

    def _add_to_queue(self, label):
        if label.get_node_id() not in self._closed_set:
            print("Added " + label.__str__())
            self._queue.put((label.get_cost(), label))
