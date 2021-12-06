from cost_functions import *
from graph import *
from search_algs import *
from collisions import *

if __name__ == "__main__":
    graph_path = '../test_cases/aalborg_storcenter.json'
    graph = Graph(graph_path)

    # get all shortest paths
    alg = BulkSearchAlgorithm(graph.get_nodes_with_people(), graph, EdgeCostFunction())

    shortest_paths = alg.search()

    for p in shortest_paths:
        print(p)

    # find collisions between shortest paths
    collisions = identify_all_collisions(shortest_paths, graph)
    collisions = merge_collision(collisions)

    # create all possible constraints for one of the collisions
    constraints_for_first_collision = collisions[0].get_all_constraints()
