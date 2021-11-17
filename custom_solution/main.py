from cost_functions import *
from graph import *
from search_algs import *

if __name__ == "__main__":
    graph_path = '../test_cases/aalborg_storcenter.json'
    #print(" ==== LOADING GRAPH from %s ====" % graph_path)
    graph = Graph(graph_path)

    alg = BulkSearchAlgorithm(graph.get_nodes_with_people(), graph, EdgeCostFunction())

    alg_search = alg.search()

    class Collision:
        _travel_time = []
        _edge = []
        _paths = []

        def __init__(self, path1, path2, edge):
            #unsure about what the travel_time is 
            self._travel_time.append(path1.get_timing())
            self._travel_time.append(path2.get_timing())
            self._edge = edge
            self._paths.append(path1.get_path())
            self._paths.append(path2.get_path())
    
    collisions = []
    
    for i in range(len(alg_search)):
        collision_edge = []
        
        for j in range(i, len(alg_search)):

            if i != j:

                for path_1, path_2, timestep_1, timestep_2 in zip(alg_search[i].get_path(), alg_search[j].get_path(), alg_search[i].get_timing(), alg_search[j].get_timing()):
                    if path_1 == path_2 and timestep_1 == timestep_2:
                        collision_edge.append(path_1)

                    if len(collision_edge) == 2:
                        collisions.append(Collision(i, j, collision_edge))
                        collision_edge = []
                
                    if path_1 != path_2 and len(collision_edge) != 0:
                        collision_edge.pop()


