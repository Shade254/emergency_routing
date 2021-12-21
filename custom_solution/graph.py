import json

from shapely import ops
from shapely.geometry import LineString, MultiLineString, Point, Polygon

from risk_functions import *
from utils import transform


class Node:
    def __init__(self, node_feature):
        self.name = ''
        self.is_exit = False
        self.risk = ConstantFunction(1)
        self.people = 0
        self.geojson = node_feature['geometry']
        self.geometry = Point(transform(node_feature['geometry']['coordinates'][1], node_feature['geometry']['coordinates'][0], 2197))
        if 'name' not in node_feature['properties']:
            self.name = hash(self.geojson.__str__()) % 100000
        else:
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
    def __init__(self, from_id, to_id, capacity, risk, travel_time, geometry, geojson):
        self.from_node = from_id
        self.to_node = to_id
        self.capacity = capacity
        self.risk = risk
        self.travel_time = travel_time
        self.geometry = geometry
        self.geojson = geojson
        self.oneway = False

    @staticmethod
    def create_from_feature(edge_feature):
        # infinite capacity
        capacity = ConstantFunction(1)
        risk = ConstantFunction(1)
        from_node = ''
        to_node = ''
        # constant travel time for the sake of simplicity
        travel_time = 1

        projected_coordinates = []
        for a in edge_feature['geometry']['coordinates']:
            projected_coordinates.append(transform(a[1], a[0], 2197))

        geometry = LineString(projected_coordinates)
        geojson = edge_feature['geometry']

        if 'capacity' in edge_feature['properties']:
            capacity = CapacityFunction(edge_feature['properties']['capacity'])

        if 'risk' in edge_feature['properties']:
            risk = ConstantFunction(edge_feature['properties']['risk'])

        from_node = edge_feature['properties']['from']
        to_node = edge_feature['properties']['to']
        return Edge(from_node, to_node, capacity, risk, travel_time, geometry, geojson)

    @staticmethod
    def merge_two_edges(from_id, to_id, edge1, edge2):
        new_risk = edge1.risk
        if edge1.risk != edge2.risk:
            if edge1.risk.get_risk(0) < edge2.risk.get_risk(0):
                new_risk = edge2.risk

        if not isinstance(edge1.capacity, ConstantFunction) and not isinstance(edge2.capacity, ConstantFunction):
            raise ValueError("Cannot raise two non-trivial capacity functions")

        new_capacity = edge1.capacity
        if not isinstance(edge2.capacity, ConstantFunction):
            new_capacity = edge2.capacity

        new_geometry = MultiLineString([edge1.geometry, edge2.geometry])
        new_geometry = ops.linemerge(new_geometry)

        new_geojson = {
            "type"       : "LineString",
            "coordinates": []
            }

        for c in edge1.geojson['coordinates']:
            new_geojson['coordinates'].append(c)

        second = edge2.geojson['coordinates']

        if second[0] == new_geojson['coordinates'][-1]:
            second = second[1:]
        elif second[-1] == new_geojson['coordinates'][-1]:
            second = second[:-1]
            second.reverse()
        elif second[0] == new_geojson['coordinates'][0]:
            second = second[1:]
            new_geojson['coordinates'].reverse()
        else:
            second = second[:-1]
            second.reverse()
            new_geojson['coordinates'].reverse()

        for c in second:
            new_geojson['coordinates'].append(c)

        return Edge(from_id, to_id, new_capacity, new_risk, 1, new_geometry, new_geojson)

    def create_opposite(self):
        return Edge(self.to_node, self.from_node, self.capacity, self.risk, self.travel_time, self.geometry, self.geojson)

    def __str__(self):
        return "Edge %s->%s, capacity=%s, risk=%s, travel_time=%d" % (self.from_node, self.to_node, self.capacity.__str__(), self.risk.__str__(), self.travel_time)

    def __hash__(self):
        return hash((self.from_node, self.to_node))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


class Area:
    def __init__(self, area_feature):
        self.type = area_feature['properties']['type']
        self.risk = ConstantFunction(area_feature['properties']['risk'])

        projected_coords = []
        for c in area_feature["geometry"]["coordinates"][0]:
            projected_coords.append(transform(c[1], c[0], 2197))
        self.geometry = Polygon(projected_coords)
        self.geojson = area_feature['geometry']

    def __str__(self):
        return "Area type=%s, risk=%s" % (self.type, self.risk.__str__())


class Graph:
    def __init__(self, path_to_graph, path_to_data=None):
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
            for node_id in self.__node_map:
                self.__add_edge_to_graph(node_id, node_id, Edge(node_id, node_id, ConstantFunction(0), self.__node_map[node_id].risk, 1, self.__node_map[node_id].geometry,
                                                                self.__node_map[node_id].geojson))

        if path_to_data:
            print("Loading data from file " + path_to_data)
            with open(path_to_data, 'r') as f:
                lines = f.readlines()
                first = True
                for line in lines:
                    if first:
                        first = False
                        continue

                    splitted = line.split(",")
                    if len(splitted) == 3 and splitted[0] in self.__node_map:
                        self.__node_map[splitted[0]].people = int(splitted[1])
                        self.__node_map[splitted[0]].is_exit = splitted[2] == "True"

    def contract_nodes(self):
        nodes_to_contract = []
        for n in self.__node_map:
            if self.__node_map[n].is_exit:
                continue
            out_edges = [x for x in self.__edge_map[n].keys()]
            out_edges.remove(n)
            in_edges = []
            for n1 in self.__node_map:
                if n1 != n and n in self.__edge_map[n1]:
                    in_edges.append(n1)

            out_edges.sort()
            in_edges.sort()

            # transit node
            if out_edges == in_edges and len(out_edges) == 2:
                nodes_to_contract.append(n)

        print("Removing %d nodes" % len(nodes_to_contract))
        for n in nodes_to_contract:
            print("Removing transit node " + n)
            out = [x.to_node for x in self.get_out_edges(n)]
            out.remove(n)

            new_from = out[0]
            new_to = out[1]

            if self.get_edge(new_from, new_to):
                continue

            new_edge = Edge.merge_two_edges(new_from, new_to, self.__edge_map[new_from][n], self.__edge_map[n][new_to])
            opposite_edge = new_edge.create_opposite()

            self.remove_edge(n, n)
            self.remove_edge(new_from, n)
            self.remove_edge(n, new_from)
            self.remove_edge(new_to, n)
            self.remove_edge(n, new_to)
            self.remove_node(n)
            self.__add_edge_to_graph(new_from, new_to, new_edge)
            self.__add_edge_to_graph(new_to, new_from, opposite_edge)
            self.num_of_edges -= 3

    def output_geojson(self, file="graph.json"):
        with open(file, "w") as opened_file:
            features = []

            for n, node in self.__node_map.items():
                if not node:
                    continue

                f = {
                    "type"      : "Feature",
                    "properties": {
                        "name": n,
                        },
                    "geometry"  : node.geojson
                    }
                features.append(f)
            closed_set = []
            for e in self.get_all_edges():
                if not e or e.from_node == e.to_node or (e.from_node, e.to_node) in closed_set:
                    continue

                f = {
                    "type"      : "Feature",
                    "properties": {
                        "from": e.from_node,
                        "to"  : e.to_node
                        },
                    "geometry"  : e.geojson
                    }
                features.append(f)
                closed_set.append((e.from_node, e.to_node))
                closed_set.append((e.to_node, e.from_node))
            for a in self.area_list:
                f = {
                    "type"      : "Feature",
                    "properties": {
                        "type": a.type,
                        "risk": a.risk.get_risk(0)
                        },
                    "geometry"  : a.geojson
                    }
                features.append(f)

            collection = {
                "type"    : "FeatureCollection",
                "features": features}
            opened_file.write(json.dumps(collection))

    def __add_edge_to_graph(self, from_id, to_id, edge):
        if from_id not in self.__edge_map:
            self.__edge_map[from_id] = {}

        if to_id not in self.__edge_map[from_id]:
            self.__edge_map[from_id][to_id] = edge
        else:
            raise ValueError('Edge ' + from_id + "->" + to_id + " is already in the graph")

    def get_all_nodes(self):
        return self.__node_map.keys()

    def remove_edge(self, from_id, to_id):
        if from_id in self.__edge_map and to_id in self.__edge_map[from_id]:
            self.__edge_map[from_id].pop(to_id)
            return True
        return False

    def remove_node(self, node_id):
        if node_id in self.__node_map:
            self.__node_map.pop(node_id)
            return True
        return False

    def get_nodes_with_people(self):
        node_people_dict = {}
        for n in self.get_all_nodes():
            node = self.get_node(n)
            if node.people > 0:
                node_people_dict[n] = node.people
        return node_people_dict

    def get_node(self, node_id):
        if node_id not in self.__node_map:
            return None
        return self.__node_map[node_id]

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

    @staticmethod
    def __assert_risk(areas, edges, nodes):
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
