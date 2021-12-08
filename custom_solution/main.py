from os import pardir
from sys import path
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

    print("--------------")


    bounded_paths = []
    
    for i in shortest_paths: 
        path = i.get_path()
        upper_bound = 0
        for j in range(len(path)-1):
            for c in collisions:
                if c.edge.from_node == path[j] and c.edge.to_node == path[j + 1]: 
                    upper_bound += EdgeCostFunction.get_risk(c.people, c.edge)
                else: 
                    edge = graph.get_edge(path[j], path[j + 1])
                    upper_bound += EdgeCostFunction.get_risk(path.people, edge)

        
        bounded_paths.append(BoundedPath(path, upper_bound))

    
        
        


        #print("....................")
