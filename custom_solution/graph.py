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


class Area:
    def __init__(self, area_feature):
        self.type = ''
        self.risk = ConstantFunction(0)

        self.type = area_feature['properties']['type']
        self.risk = ConstantFunction(area_feature['properties']['risk'])

        # save Shaply object to this variable
        self.geometry = None


class Graph:
    def __init__(self, edge_feature):
        self.node_list = []
        self.edge_list = []
        self.area_list = []

        with open(edge_feature, 'r') as f:
            data = json.load(f)

            for i in data['features']:
                if i['geometry']['type'] == 'Point':
                    node_obj = Node(i)
                    self.node_list.append(node_obj)
                elif i['geometry']['type'] == 'LineString':
                    edge_obj = Edge(i)
                    self.edge_list.append(edge_obj)
                else:
                    area_obj = Area(i)
                    self.area_list.append(area_obj)

            print("Loaded %d nodes, %d edges and %d areas" % (len(self.node_list), len(self.edge_list), len(self.area_list)))

    def assert_risk(self, areas, edges, nodes):
        for a in areas:
            # propagate risk from area to nodes and edges that it contains
            for e in edges:
                pass
            for n in nodes:
                pass
