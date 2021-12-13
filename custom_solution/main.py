from cost_functions import *
from graph import *
from search_algs import *
from collisions import *

if __name__ == "__main__":
    graph_path = '../test_cases/aalborg_storcenter/aalborg_storcenter.json'
    data_path = '../test_cases/aalborg_storcenter/aalborg_storcenter.csv'
    graph = Graph(graph_path, data_path)

    # get all shortest paths
    alg = BulkSearchAlgorithm(graph.get_nodes_with_people(), graph, EdgeCostFunction())

    shortest_paths = alg.search()

    for p in shortest_paths:
        print(p)

    # find collisions between shortest paths
    all_collisions = identify_all_collisions(shortest_paths, graph)

    bounded_paths = get_bounded_paths(graph, shortest_paths, all_collisions)

    for i in bounded_paths:
        print(i)
        i.output_geojson(i.get_path(), i.get_people(), graph, "%s_%d_0.json" % (i.get_path()[0], i.get_people()))

    picked_collision = all_collisions[0]

    print("Picked: %s" % picked_collision)

    for path in picked_collision.get_participants():
        constraint = picked_collision.get_negative_constraint(path)
        alg = ConstrainedExitDijkstra(path.get_path()[0], path.get_people(), graph, EdgeCostFunction(), [constraint])
        i = alg.search()[0]
        print(i)
        i.output_geojson(i.get_path(), i.get_people(), graph, "%s_%d_1.json" % (i.get_path()[0], i.get_people()))

    for path in picked_collision.get_participants():
        constraint = picked_collision.get_positive_constraints(path)
        print(constraint)
        alg = ConstrainedExitDijkstra(path.get_path()[0], path.get_people(), graph, EdgeCostFunction(), [constraint])
        i = alg.search()[0]
        print(i)
        i.output_geojson(i.get_path(), i.get_people(), graph, "%s_%d_2.json" % (i.get_path()[0], i.get_people()))
