import copy

from cost_functions import *
from graph import *
from search_algs import *
from collisions import *


def choose_collision(collisions):
    return collisions[0]


def search(replan_from, replan_people, paths, constraints, graph):
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

    # return set of paths as result if no collisions detected
    if not collisions:
        return paths

    # choose specific collision to solve (in child nodes)
    to_solve = choose_collision(collisions)

    for i in range(len(to_solve.paths)):
        # for every path participating in the collision get a constraint
        replan = to_solve.paths[i]
        new_constraint = to_solve.get_constraint(i)

        # get all the other paths
        other_paths = copy.deepcopy(paths)
        other_paths.remove(replan)

        # get all the previous constraints and add a new one
        all_constraints = copy.deepcopy(constraints)
        all_constraints.append(new_constraint)

        # run recursive search with path to replan and all the constraints
        search(replan.get_path()[0], replan.get_people(), other_paths, constraints, graph)


if __name__ == "__main__":
    graph_path = '../test_cases/aalborg_storcenter/aalborg_storcenter.json'
    data_path = '../test_cases/aalborg_storcenter/aalborg_storcenter.csv'
    graph = Graph(graph_path, data_path)

    # get all shortest paths
    alg = BulkSearchAlgorithm(graph.get_nodes_with_people(), graph, EdgeCostFunction())

    shortest_paths = alg.search()

    for p in shortest_paths:
        print(p)

    # find collisions between shortest paths
    all_collisions = identify_all_collisions(shortest_paths, graph)

    bounded_paths = get_bounded_paths(graph, shortest_paths, all_collisions)

    for i in bounded_paths:
        print(i)
        i.output_geojson(i.get_path(), i.get_people(), graph, "%s_%d_0.json" % (i.get_path()[0], i.get_people()))

    picked_collision = all_collisions[0]

    print("Picked: %s" % picked_collision)

    for path in picked_collision.get_participants():
        constraint = picked_collision.get_negative_constraint(path)
        alg = ConstrainedExitDijkstra(path.get_path()[0], path.get_people(), graph, EdgeCostFunction(), [constraint])
        i = alg.search()[0]
        print(i)
        i.output_geojson(i.get_path(), i.get_people(), graph, "%s_%d_1.json" % (i.get_path()[0], i.get_people()))

    for path in picked_collision.get_participants():
        constraint = picked_collision.get_positive_constraints(path)
        print(constraint)
        alg = ConstrainedExitDijkstra(path.get_path()[0], path.get_people(), graph, EdgeCostFunction(), [constraint])
        i = alg.search()[0]
        print(i)
        i.output_geojson(i.get_path(), i.get_people(), graph, "%s_%d_2.json" % (i.get_path()[0], i.get_people()))
