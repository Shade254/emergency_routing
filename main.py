import json

class Node:

    node_name = ''     
    node_is_exit = False
    node_gType = ''
    node_coordinates = []
    node_risk  = 0
    node_people = {}

    def __init__(self, graph_data):

        self.node_name = graph_data['properties']['name']

        if 'is_exit' in graph_data['properties']:
            self.node_is_exit = True

        self.node_gType = graph_data['geometry']['type']
        self.node_coordinates = graph_data['geometry']['coordinates']

        if 'risk' in graph_data['properties']: 
            self.node_risk = graph_data['properties']['risk']

        if 'people' in graph_data['properties']:
            #self.node_people = graph_data['properties']['people']
            pass
            ##Trouble converting the input from string to another type

class Edge:

    edge_capacity = {} 
    edge_risk = 0
    edge_from_node = ''
    edge_to_node = ''
    edge_gType = ''
    edge_coordinates = []

    #edge_travel_time = 0
    #edge_type = ''
    #edge_oneway = False

    def __init__(self, graph_data): 
        
        if 'capacity' in graph_data['properties']: 
            #self.edge_capacity = graph_data['properties']['capacity']
            pass
            #Trouble converting the input from string to another type

        if 'risk' in graph_data['properties']: 
            self.edge_risk = graph_data['properties']['risk']
        
        self.edge_from_node = graph_data['properties']['from']
        self.edge_to_node = graph_data['properties']['to']
        self.edge_gType = graph_data['geometry']['type']
        self.edge_coordinates = graph_data['geometry']['coordinates']

class Area: 

    area_type = ''
    area_risk = 0
    area_gType = ''
    area_coordinates = []

    def __init__(self, graph_data): 

        self.area_type = graph_data['properties']['type']
        self.area_risk = graph_data['properties']['risk']
        self.area_gType = graph_data['geometry']['type']
        self.area_coordinates = graph_data['geometry']['coordinates']
        
class Graph(Node, Edge, Area): 

    node_list = []
    edge_list = []
    area_list = []

    def __init__(self, graph_data):
        f = open(graph_data,)
        data = json.load(f)

        for i in data['features']:
            if i['geometry']['type'] == 'Point': 
                NodeObj = Node(i)
                self.node_list.append(NodeObj)
            elif i['geometry']['type'] == 'LineString': 
                EdgeObj = Edge(i)
                self.edge_list.append(EdgeObj) 
            elif i['geometry']['type'] == 'Polygon': 
                AreaObj = Area(i) 
                self.area_list.append(AreaObj)
                

test_load = Graph('test_cases/aalborg_storcenter.json')










