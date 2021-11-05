from cost_functions import *
from graph import *
from search_algs import *

if __name__ == "__main__":
    graph_path = '../test_cases/aalborg_storcenter.json'
    print(" ==== LOADING GRAPH from %s ====" % graph_path)
    graph = Graph(graph_path)

    alg = BulkSearchAlgorithm(graph.get_nodes_with_people(), graph, EdgeCostFunction())
    print(len(alg.search()))
