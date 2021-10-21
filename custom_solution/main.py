from graph import *

if __name__ == "__main__":
    loaded_graph = Graph('../test_cases/aalborg_storcenter.json')
    print(loaded_graph.get_node("center"))
    print(loaded_graph.get_node("exit_a"))
    print(loaded_graph.get_edge("center", "crossroad_2"))
    print(loaded_graph.get_edge("crossroad_1", "crossroad_4"))
    print(loaded_graph.get_edge("crossroad_4", "crossroad_1"))
    print(loaded_graph.get_out_edges("crossroad_4"))
