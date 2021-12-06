from paths import *
from label_factories import *
from goal_checkers import *
from heuristics import *
from queue import PriorityQueue


# base class for every search algorithm
# takes from queue, checks against closed set, check for goal, expands with label factory
# queue ordering is defined in child classes
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
            # print("Number of children: %d" % len(children))
            for label in children:
                self._add_to_queue(label)
            self._closed_set.append(current_label.get_node_id())

        return self._reconstruct_paths(end_labels)


# class that is parent for all search algorithms that have goal checker and label factory creation wired in
# i.e. you  provide only start node (not start labels), people, graph and cost function
class SelfContainedSearchAlg(SearchAlgorithm):
    def __init__(self, start_node_name, people, graph, cost_function):
        goal_checker = self._create_goal_checker()
        label_factory = self._create_label_factory(graph, cost_function)
        start_labels = label_factory.get_start_labels(start_node_name, people)
        super().__init__(start_labels, label_factory, goal_checker)

    def _create_goal_checker(self):
        pass

    def _create_label_factory(self, graph, cost_function):
        pass


# base class for all search algorithms that have only one target (goal checker is initialized to check for only end_node_name)
class SimpleSearchAlg(SelfContainedSearchAlg):
    def __init__(self, start_node_name, people, end_node_name, graph, cost_function):
        self._end_node_name = end_node_name
        super().__init__(start_node_name, people, graph, cost_function)

    def _create_goal_checker(self):
        return SingleNodeGoalChecker(self._end_node_name)


# base class for Dijkstra algorithms
# defines label factory  without heuristic and queue ordering according to the cost
class Dijkstra(SelfContainedSearchAlg):
    def _add_to_queue(self, label):
        if label.get_node_id() not in self._closed_set:
            self._queue.put((label.get_cost(), label))

    def _create_label_factory(self, graph, cost_function):
        return CostLabelFactory(graph, cost_function)


# base class for AStar algorithms
# defines label factory  with heuristic and queue ordering according to the cost+heuristic
class AStar(SelfContainedSearchAlg):
    def _add_to_queue(self, label):
        if label.get_node_id() not in self._closed_set:
            self._queue.put((label.get_cost(), label))

    def _create_label_factory(self, graph, cost_function):
        return HeuristicCostLabelFactory(graph, cost_function, self._heuristic)


# Dijkstra algorithm with single goal
class SimpleDijkstra(SimpleSearchAlg, Dijkstra):
    def __init__(self, start_node_name, people, end_node_name, graph, cost_function):
        super().__init__(start_node_name, people, end_node_name, graph, cost_function)


# AStar algorithm with single goal
class SimpleAStar(SimpleSearchAlg, AStar):
    def __init__(self, start_node_name, people, end_node_name, graph, cost_function, heuristic=None):
        if not heuristic:
            heuristic = ConstantHeuristic(graph, [end_node_name], 1)
        self._heuristic = heuristic
        super().__init__(start_node_name, people, end_node_name, graph, cost_function)


# Parent for search algorithms that end search in any exit node
class ExitSearchAlg(SelfContainedSearchAlg):
    def __init__(self, start_node_name, people, graph, cost_function):
        self._graph = graph
        super().__init__(start_node_name, people, graph, cost_function)

    def _create_goal_checker(self):
        return ExitGoalChecker(self._graph)


# Dijkstra algorithm with every exit as a goal
class ExitDijkstra(ExitSearchAlg, Dijkstra):
    def __init__(self, start_node_name, people, graph, cost_function):
        super().__init__(start_node_name, people, graph, cost_function)

# constrained Dijkstra algorithm with every exit as a goal
class ConstrainedExitDijkstra(ExitSearchAlg, Dijkstra):
    def __init__(self, start_node_name, people, graph, cost_function, constraints):
        self.constraints = constraints
        super().__init__(start_node_name, people, graph, cost_function)
    
    def _create_label_factory(self, graph, cost_function):
        return ConstrainedCostLabelFactory(graph, cost_function, self.constraints)



# AStar algorithm with every exit as a goal
class ExitAStar(ExitSearchAlg, AStar):
    def __init__(self, start_node_name, people, graph, cost_function, heuristic=None):
        if not heuristic:
            heuristic = ConstantHeuristic(graph, [], 0)
        self._heuristic = heuristic
        super().__init__(start_node_name, people, graph, cost_function)


class BulkSearchAlgorithm:
    def __init__(self, nodes_people_dict, graph, cost_function, heuristic=None):
        self._starts = nodes_people_dict
        self._graph = graph
        self._cost_function = cost_function
        self._heuristic = heuristic

    def search(self):
        shortest_paths = []
        for node, people in self._starts.items():
            if self._heuristic:
                algorithm = ExitAStar(node, people, self._graph, self._cost_function, self._heuristic)
            else:
                algorithm = ExitDijkstra(node, people, self._graph, self._cost_function)

            paths = algorithm.search()
            print("%d paths found from %s for %d people" % (len(paths), node, people))
            for p in paths:
                print(p)
                print("TIMING: " + p.get_timing().__str__())
            shortest_paths.extend(paths)
        return shortest_paths
