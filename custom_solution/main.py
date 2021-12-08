from cost_functions import *
from graph import *
from search_algs import *
from collisions import *


def add_bound_to_path(simple_path, collisions):
    path = simple_path.get_path()
    upper_bound = 0
    for j in range(len(path) - 1):
        active_collisions = []
        for c in collisions:
            if c.edge.from_node == path[j] and c.edge.to_node == path[j + 1] and c.when == j:
                active_collisions.append(c)

        edge = graph.get_edge(path[j], path[j + 1])
        if not active_collisions:
            upper_bound += EdgeCostFunction.get_risk(simple_path.people, edge)
        else:
            active_people = simple_path.people
            for c in active_collisions:
                active_people += c.people - simple_path.people

            upper_bound += EdgeCostFunction.get_risk(active_people, edge)

    return BoundedPath(simple_path, upper_bound)


if __name__ == "__main__":
    graph_path = '../test_cases/aalborg_storcenter.json'
    graph = Graph(graph_path)

    # get all shortest paths
    alg = BulkSearchAlgorithm(graph.get_nodes_with_people(), graph, EdgeCostFunction())

    shortest_paths = alg.search()

    for p in shortest_paths:
        print(p)

    # find collisions between shortest paths
    all_collisions = identify_all_collisions(shortest_paths, graph)

    # create all possible constraints for one of the collisions
    constraints_for_first_collision = all_collisions[0].get_all_constraints()

    print("--------------")

    bounded_paths = []

    for i in shortest_paths:
        bounded_paths.append(add_bound_to_path(i, all_collisions))

    for i in bounded_paths:
        print(i)
