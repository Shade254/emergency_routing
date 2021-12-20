import getopt
import sys
import time

from collisions import *
from custom_solution.cbs import search
from graph import *
from search_algs import *

if __name__ == "__main__":

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "g:p:t:e:b:h")
    except:
        print("Cannot load input arguments")
        sys.exit(1)

    data_path = None
    time_limit = None
    graph_path = None
    tolerance = 0
    bounds = True

    for opt, arg in opts:
        if opt in ['-g']:
            graph_path = arg
        elif opt in ['-p']:
            data_path = arg
        elif opt in ['-t']:
            time_limit = int(arg)
        elif opt in ['-e']:
            tolerance = float(arg)
        elif opt in ['-b']:
            bounds = opt == "True"
        elif opt in ['-h']:
            print("Usage:")
            print("-g path to geojson file with graph (required)")
            print("-p path to csv file with people")
            print("-t time limit (default - not set)")
            print("-e epsilon tolerance for an optimal result (default - 0)")
            print("-b use bounds to prune recursive search True/False (default - True)")
            sys.exit(0)

    if not graph_path:
        print("Error: Path to graph required!")
        print("Use -h option to print out usage of the script")
        sys.exit(-1)

    print("INIT PARAMS:")
    print("Graph  : " + graph_path)
    print("People : " + str(data_path))
    print("Limit  : " + str(time_limit) + "s")
    print("Epsilon: " + str(tolerance))
    print("Bounds : " + str(bounds))

    graph = Graph(graph_path, data_path)

    start_time = time.time()
    end_time = None
    if time_limit:
        end_time = time.time() + time_limit

    print("\n\n Initiallized ... getting shortest paths to the nearest exit ... \n\n")

    # get all shortest paths
    alg = BulkSearchAlgorithm(graph.get_nodes_with_people(), graph, EdgeCostFunction())
    shortest_paths = alg.search()

    print("\n\n Starting recursion ... \n\n")

    init_bounds = None
    if bounds:
        lower_bound = 0
        for p in shortest_paths:
            lower_bound += p.get_cost() * p.get_people()
        init_bounds = (lower_bound, sys.maxsize)

    result = search(None, None, shortest_paths, init_bounds, {}, graph, [], end_time, tolerance)

    print("\nAlgorithm done in %d iterations and %f milliseconds" % (result.iterations, (time.time() - start_time) * 1000))

    print("\nBest result is:")
    print(result)
