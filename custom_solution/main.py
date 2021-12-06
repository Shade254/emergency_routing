from cost_functions import *
from graph import *
from search_algs import *
from collisions import *

if __name__ == "__main__":
    graph_path = '../test_cases/aalborg_storcenter.json'
    graph = Graph(graph_path)

    alg = ExitDijkstra("toilets", 10, graph, EdgeCostFunction())
    result = alg.search()
    for i in result: 
        print(i)
    

    constraints = Constraint(graph.get_edge("crossroad_2", "crossroad_1"), 1, 10)

    alg = ConstrainedExitDijkstra("toilets", 10, graph, EdgeCostFunction(), [constraints])
    result = alg.search()
    for i in result: 
        print(i)


