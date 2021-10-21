import json
from risk_functions import *


class Node:
    def __init__(self, node_feature):
        self.name = ''
        self.is_exit = False
        self.risk = ConstantFunction(0)
        self.people = 0

        # save Shaply object to this variable
        self.geometry = None

        self.name = node_feature['properties']['name']

        if 'is_exit' in node_feature['properties'] and node_feature['properties']['is_exit']:
            self.is_exit = True

        if 'risk' in node_feature['properties']:
            self.risk = ConstantFunction(node_feature['properties']['risk'])

        if 'people' in node_feature['properties']:
            self.people = node_feature['properties']['people']['normal']

    def __str__(self):
        str = ""
        if self.is_exit:
            str = "(exit) "
        str += "Node %s, people=%d, risk=%s" % (self.name, self.people, self.risk.__str__())
        return str


class Edge:
    def __init__(self, edge_feature):
        # infinite capacity
        self.capacity = ConstantFunction(0)
        self.risk = ConstantFunction(0)
        self.from_node = ''
        self.to_node = ''
        # constant travel time for the sake of simplicity
        self.travel_time = 1
        self.oneway = False

        # save Shaply object to this variable
        self.geometry = None

        if 'capacity' in edge_feature['properties']:
            self.capacity = CapacityFunction(edge_feature['properties']['capacity'])

        if 'risk' in edge_feature['properties']:
            self.risk = ConstantFunction(edge_feature['properties']['risk'])

        self.from_node = edge_feature['properties']['from']
        self.to_node = edge_feature['properties']['to']

    def __str__(self):
        str = "Edge %s->%s, capacity=%s, risk=%s, travel_time=%d" % (self.from_node, self.to_node, self.capacity.__str__(), self.risk.__str__(), self.travel_time)
        return str


class Area:
    def __init__(self, area_feature):
        self.type = ''
        self.risk = ConstantFunction(0)

        self.type = area_feature['properties']['type']
        self.risk = ConstantFunction(area_feature['properties']['risk'])

        # save Shaply object to this variable
        self.geometry = None

    def __str__(self):
        str = "Area type=%s, risk=%s" % (self.type, self.risk.__str__())
        return str


class Graph:
    def __init__(self, edge_feature):
        self.num_of_edges = 0
        self.__node_map = {}
        self.__edge_map = {}
        self.area_list = []

        with open(edge_feature, 'r') as f:
            data = json.load(f)

            for i in data['features']:
                if i['geometry']['type'] == 'Point':
                    node_obj = Node(i)
                    if node_obj.name in self.__node_map:
                        raise ValueError("ID " + node_obj.name + " appeared twice in the graph")
                    self.__node_map[node_obj.name] = node_obj
                elif i['geometry']['type'] == 'LineString':
                    edge_obj = Edge(i)
                    self.__add_edge_to_graph(edge_obj.from_node, edge_obj.to_node, edge_obj)
                    self.num_of_edges += 1
                    if not edge_obj.oneway:
                        self.__add_edge_to_graph(edge_obj.to_node, edge_obj.from_node, edge_obj)
                        self.num_of_edges += 1
                else:
                    area_obj = Area(i)
                    self.area_list.append(area_obj)

            print("Loaded %d nodes, %d edges and %d areas" % (len(self.__node_map), self.num_of_edges, len(self.area_list)))
            print("Propagating risk from areas to nodes and edges")
            self.__assert_risk(self.area_list, self.__edge_map, self.__node_map)

    def __add_edge_to_graph(self, from_id, to_id, edge):
        if from_id not in self.__edge_map:
            self.__edge_map[from_id] = {}

        if to_id not in self.__edge_map[from_id]:
            self.__edge_map[from_id][to_id] = edge
        else:
            raise ValueError('Edge ' + from_id + "->" + to_id + " is already in the graph")

    def get_node(self, id):
        if id not in self.__node_map:
            return None
        return self.__node_map[id]

    def get_edge(self, from_id, to_id):
        if from_id in self.__edge_map and to_id in self.__edge_map[from_id]:
            return self.__edge_map[from_id][to_id]
        return None

    def get_out_edges(self, node_id):
        if node_id in self.__edge_map:
            return self.__edge_map[node_id]
        return None

    def __assert_risk(self, areas, edges, nodes):
        for a in areas:
            # propagate risk from area to nodes and edges that it contains
            for e in edges:
                pass
            for n in nodes:
                pass