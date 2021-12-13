import copy
from dataclasses import dataclass

from cost_functions import *
from graph import *
from search_algs import *
from collisions import *


def choose_collision(collisions):
    return collisions[0]


@dataclass(frozen=False)
class Result:
    lower_bound: int
    upper_bound: int
    paths: [Path]

    def __str__(self):
        strrr = "COST (%d, %d)\n" % (self.lower_bound, self.upper_bound)
        for p in self.paths:
            strrr += "\t" + p.__str__() + "\n"
        return strrr


def get_bound(paths):
    upper = 0
    lower = 0
    for p in paths:
        upper += p.upper_bound * p.get_people()
        lower += p.get_cost() * p.get_people()
    return lower, upper


def pick_best_result(results):
    if not results:
        return None
    return sorted(results, key=lambda x: x.upper_bound)[0]


def search(replan_from, replan_people, paths, constraints, graph, solved_collisions):
    if replan_from and replan_people:
        # replan specific path if chosen by parent node
        new_alg = ConstrainedExitDijkstra(replan_from, replan_people, graph, EdgeCostFunction(), constraints)
        new_paths = new_alg.search()
        # fail if replanning not possible
        if not new_paths:
            print("No replanning possible for " + constraints)
            return None
        paths.append(new_paths[0])

    # detect collisions between all paths
    collisions = identify_all_collisions(paths, graph)
    for c in solved_collisions:
        collisions.remove(c)

    # return set of paths as result if no collisions detected
    if not collisions:
        return paths

    # choose specific collision to solve (in child nodes)
    to_solve = choose_collision(collisions)

    new_solved_collisions = copy.deepcopy(solved_collisions)
    new_solved_collisions.append(to_solve)

    results = []

    for path in to_solve.get_participants():
        new_replan_from = path.get_path()[0]
        new_replan_people = path.get_path()[0]

        negative_constraint = to_solve.get_negative_constraint(path)

        # get all the other paths
        other_paths = copy.deepcopy(paths)
        other_paths.remove(path)

        # get all the previous constraints and add a new one
        all_constraints = copy.deepcopy(constraints)
        all_constraints[new_replan_from].append(negative_constraint)

        # run recursive search with path to replan and all the constraints
        results.append(search(new_replan_from, new_replan_people, other_paths, all_constraints, graph, new_solved_collisions))

    all_constraints = copy.deepcopy(constraints)
    for path in to_solve.get_participants():
        positive_constraint = to_solve.get_positive_constraint(path)
        all_constraints[path.get_path()[0]].append(positive_constraint)

    other_paths = copy.deepcopy(paths)
    results.append(search(None, None, other_paths, all_constraints, graph, new_solved_collisions))
    return pick_best_result(results)


if __name__ == "__main__":
    graph_path = '../test_cases/aalborg_storcenter/aalborg_storcenter.json'
    data_path = '../test_cases/aalborg_storcenter/aalborg_storcenter.csv'
    graph = Graph(graph_path, data_path)

    # get all shortest paths
    alg = BulkSearchAlgorithm(graph.get_nodes_with_people(), graph, EdgeCostFunction())
    shortest_paths = alg.search()

    result = search(None, None, shortest_paths, {}, graph, [])
    print(result)
