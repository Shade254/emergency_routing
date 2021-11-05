from graph import *
from search_algs import *
from cost_functions import *
from heuristics import *

if __name__ == "__main__":
    graph_path = '../test_cases/aalborg_storcenter.json'
    print(" ==== LOADING GRAPH from %s ====" % graph_path)
    graph = Graph(graph_path)

    from_node = "exit_a"
    to_node = "exit_b"
    print(" ==== RUNNING DIJKSTRA %s -> %s ====" % (from_node, to_node))
    dijkstra = ExitDijkstra("center", 10, graph, EdgeCostFunction())
    paths = dijkstra.search()
    print("Found %d paths" % len(paths))
    for p in paths:
        print(p)

    print(" ==== RUNNING A* %s -> %s ====" % (from_node, to_node))
    a_star = ExitAStar("center", 10, graph, EdgeCostFunction())
    paths = a_star.search()
    print("Found %d paths" % len(paths))
    for p in paths:
        print(p)
