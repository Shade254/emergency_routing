import json
from risk_functions import *
from shapely.geometry import Point, Polygon, LineString
from utils import transform


class Node:
    def __init__(self, node_feature):
        self.name = ''
        self.is_exit = False
        self.risk = ConstantFunction(0)
        self.people = 0
        self.geometry = Point(transform(node_feature['geometry']['coordinates'][1], node_feature['geometry']['coordinates'][0], 2197))
        self.name = node_feature['properties']['name']

        if 'is_exit' in node_feature['properties'] and node_feature['properties']['is_exit']:
            self.is_exit = True

        if 'risk' in node_feature['properties']:
            self.risk = ConstantFunction(node_feature['properties']['risk'])

        if 'people' in node_feature['properties']:
            self.people = node_feature['properties']['people']['normal']

    def distance(self, node):
        return node.geometry.distance(self.geometry)

    def __str__(self):
        str = ""
        if self.is_exit:
            str = "(exit) "
        str += "Node %s, people=%d, risk=%s" % (self.name, self.people, self.risk.__str__())
        return str


class Edge:
    def __init__(self, from_id, to_id, capacity, risk, travel_time, geometry):
        self.from_node = from_id
        self.to_node = to_id
        self.capacity = capacity
        self.risk = risk
        self.travel_time = travel_time
        self.geometry = geometry
        self.oneway = False

    @staticmethod
    def create_from_feature(edge_feature):
        # infinite capacity
        capacity = ConstantFunction(0)
        risk = ConstantFunction(0)
        from_node = ''
        to_node = ''
        # constant travel time for the sake of simplicity
        travel_time = 1

        projected_coordinates = []
        for a in edge_feature['geometry']['coordinates']:
            projected_coordinates.append(transform(a[1], a[0], 2197))

        geometry = LineString(projected_coordinates)

        if 'capacity' in edge_feature['properties']:
            capacity = CapacityFunction(edge_feature['properties']['capacity'])

        if 'risk' in edge_feature['properties']:
            risk = ConstantFunction(edge_feature['properties']['risk'])

        from_node = edge_feature['properties']['from']
        to_node = edge_feature['properties']['to']
        return Edge(from_node, to_node, capacity, risk, travel_time, geometry)

    def create_opposite(self):
        return Edge(self.to_node, self.from_node, self.capacity, self.risk, self.travel_time, self.geometry)

    def __str__(self):
        str = "Edge %s->%s, capacity=%s, risk=%s, travel_time=%d" % (self.from_node, self.to_node, self.capacity.__str__(), self.risk.__str__(), self.travel_time)
        return str

    def __hash__(self):
        return hash((self.from_node, self.to_node))


class Area:
    def __init__(self, area_feature):
        self.type = ''
        self.risk = ConstantFunction(0)

        self.type = area_feature['properties']['type']
        self.risk = ConstantFunction(area_feature['properties']['risk'])

        projected_coords = []
        for c in area_feature["geometry"]["coordinates"][0]:
            projected_coords.append(transform(c[1], c[0], 2197))
        self.geometry = Polygon(projected_coords)

    def __str__(self):
        str = "Area type=%s, risk=%s" % (self.type, self.risk.__str__())
        return str


class Graph:
    def __init__(self, path_to_graph):
        self.num_of_edges = 0
        self.__node_map = {}
        self.__edge_map = {}
        self.area_list = []
        print("Loading graph from file " + path_to_graph)

        with open(path_to_graph, 'r') as f:
            data = json.load(f)

            for i in data['features']:
                if i['geometry']['type'] == 'Point':
                    node_obj = Node(i)
                    if node_obj.name in self.__node_map:
                        raise ValueError("ID " + node_obj.name + " appeared twice in the graph")
                    self.__node_map[node_obj.name] = node_obj
                elif i['geometry']['type'] == 'LineString':
                    edge_obj = Edge.create_from_feature(i)
                    self.__add_edge_to_graph(edge_obj.from_node, edge_obj.to_node, edge_obj)
                    self.num_of_edges += 1
                    if not edge_obj.oneway:
                        self.__add_edge_to_graph(edge_obj.to_node, edge_obj.from_node, edge_obj.create_opposite())
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

    def get_all_nodes(self):
        return self.__node_map.keys()

    def get_nodes_with_people(self):
        node_people_dict = {}
        for n in self.get_all_nodes():
            node = self.get_node(n)
            if node.people > 0:
                node_people_dict[n] = node.people
        return node_people_dict

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
            return [self.__edge_map[node_id][to] for to in self.__edge_map[node_id]]
        return None

    def get_all_edges(self):
        all_edges = []
        for f in self.get_all_nodes():
            all_edges.extend(self.get_out_edges(f))
        return all_edges

    def __assert_risk(self, areas, edges, nodes):
        for a in areas:
            print("In area of " + a.type + " with risk " + a.risk.__str__())

            for e in edges:
                for b in edges[e]:
                    if edges[e][b].geometry.intersects(a.geometry):
                        edges[e][b].risk = a.risk
                        print(e + " -> " + b)

            for n in nodes:
                if nodes[n].geometry.intersects(a.geometry):
                    nodes[n].risk = a.risk
                    print(n)
