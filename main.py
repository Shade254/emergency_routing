

class Node: 
    def __init__(self, graph_data):
        self.node_gType = graph_data['node']['gtype']
        self.node_name = graph_data['node']['name']
        self.node_risk  = graph_data['node']['risk']
        self.node_people = graph_data['node']['people']
        self.node_is_exit = graph_data['node']['is_exit']

class Edge:
    def __init__(self, graph_data): 
        self.edge_gType = graph_data['edge']['gtype']
        self.edge_risk = graph_data['edge']['risk']
        self.edge_capacity = graph_data['edge']['capacity']
        self.edge_travel_time = graph_data['edge']['travel_time']
        self.edge_type = graph_data['edge']['type']
        self.edge_from_node = graph_data['edge']['from']
        self.edge_to_node = graph_data['edge']['to']
        self.edge_oneway = graph_data['edge']['oneway'] 

class Area: 
    def __init__(self, graph_data): 
        self.area_gType = graph_data['area']['gtype']
        self.area_type = graph_data['area']['type']
        self.area_risk = graph_data['area']['risk']

class Graph(Node, Edge, Area): 
    def __init__(self, graph_data):
        Node.__init__(self, graph_data)
        Edge.__init__(self, graph_data)
        Area.__init__(self, graph_data)



input = { 
    "node": {"gtype":"node_placeholder", "name":"node1", "risk":0, "people":{"normal":40, "disabled":5}, "is_exit": True}, 
    "edge": {"gtype":"edge_placeholder", "risk":0, "capacity":{100:0, 300:20, 500:60, 1000:100}, "travel_time":0, "type":"placeholder", "from":"node1", "to":"node2", "oneway":True}, 
    "area": {"gtype":"area_placeholder", "type":"fire", "risk":0}
}


newGraph = Graph(input)













