import sys
import time

from collisions import *
from custom_solution.cbs import search
from graph import *
from search_algs import *

if __name__ == "__main__":
    graph_path = '../test_cases/aalborg_storcenter/aalborg_storcenter.json'
    data_path = '../test_cases/aalborg_storcenter/aalborg_storcenter.csv'
    graph = Graph(graph_path, data_path)

    # get all shortest paths
    alg = BulkSearchAlgorithm(graph.get_nodes_with_people(), graph, EdgeCostFunction())
    shortest_paths = alg.search()

    print("Initiallized ... starting recursion ... \n\n\n\n\n\n")

    lower_bound = 0
    for p in shortest_paths:
        lower_bound += p.get_cost()

    start_time = time.time()
    # time_limit = None
    time_limit = 40  # seconds
    end_time = None
    if time_limit:
        end_time = time.time() + time_limit

    result = search(None, None, shortest_paths, (lower_bound, sys.maxsize), {}, graph, [], end_time)


    print("\nAlgorithm done in %d iterations and %d seconds" % (result.iterations, (time.time() - start_time)))

    print("\nBest result is:")
    print(result)
