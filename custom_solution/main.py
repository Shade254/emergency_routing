from cost_functions import *
from graph import *
from search_algs import *
from collisions import *

if __name__ == "__main__":
    graph_path = '../test_cases/aalborg_storcenter.json'
    graph = Graph(graph_path)

    alg = BulkSearchAlgorithm(graph.get_nodes_with_people(), graph, EdgeCostFunction())

    shortest_paths = alg.search()

    for p in shortest_paths:
        print(p)

    collisions = identify_all_collisions(shortest_paths, graph)
    collisions = merge_collision(collisions)



    """
    for m in collisions:
        print(m)


    """
    print("---------------------------------")
    


    new_constraint = collisions[0].get_constraint(0) 
    print(new_constraint.return_people())


    





