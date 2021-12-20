from custom_solution.cost_functions import EdgeCostFunction
from custom_solution.paths import BoundedPath


def add_bound_to_path(graph, simple_path, collisions):
    if isinstance(simple_path, BoundedPath):
        return simple_path

    path = simple_path.get_path()
    upper_bound = 0
    for j in range(len(path) - 1):
        active_collisions = []
        for c in collisions:
            if c.edge.from_node == path[j] and c.edge.to_node == path[j + 1] and c.when == j:
                active_collisions.append(c)

        edge = graph.get_edge(path[j], path[j + 1])
        if not active_collisions:
            upper_bound += EdgeCostFunction.get_risk(simple_path.people, edge)
        else:
            active_people = simple_path.people
            for c in active_collisions:
                active_people += c.people - simple_path.people

            upper_bound += EdgeCostFunction.get_risk(active_people, edge)

    return BoundedPath(simple_path, upper_bound)


def get_bounded_paths(graph, paths, collisions):
    bounded_paths = []
    for i in paths:
        bounded_paths.append(add_bound_to_path(graph, i, collisions))
    return bounded_paths


# added graph input to get it to run
def identify_all_collisions(shortest_paths, graph):
    collisions = []

    for i in range(len(shortest_paths)):
        for j in range(i, len(shortest_paths)):
            if i != j:
                path1 = shortest_paths[i].get_path()
                timing1 = shortest_paths[i].get_timing()

                path2 = shortest_paths[j].get_path()
                timing2 = shortest_paths[j].get_timing()

                for x in range(min(len(path1), len(path2))):
                    if path1[x] == path2[x] and timing1[x] == timing2[x]:
                        if x != min(len(path1), len(path2)) - 1:
                            if path1[x + 1] == path2[x + 1]:
                                collisions.append(Collision(shortest_paths[i], shortest_paths[j],
                                                            graph.get_edge(path1[x], path1[x + 1]), timing1[x]))

    return collisions


class Constraint:
    def __init__(self, edge, when, people):
        self.edge = edge
        self.when = when
        self.people = people

    def return_people(self):
        return self.people


class NegativeConstraint(Constraint):
    def __init__(self, edge, when, people):
        super().__init__(edge, when, people)
        self.positive = False

    def __str__(self):
        return "%r %s->%s at %d with %d people" % (self.positive, self.edge.from_node, self.edge.to_node, self.when, self.people)


class PositiveConstraint(Constraint):
    def __init__(self, edge, when, people):
        super().__init__(edge, when, people)
        self.positive = True

    def __str__(self):
        return "%r %s->%s at %d with %d people" % (self.positive, self.edge.from_node, self.edge.to_node, self.when, self.people)


class Collision:
    def __init__(self, path1, path2, edge, when):
        self.edge = edge
        self.when = when
        self.path1 = path1
        self.path2 = path2
        self.people = path1.get_people() + path2.get_people()

    def get_participants(self):
        return [self.path1, self.path2]

    def get_negative_constraint(self, path):
        if path == self.path1:
            return NegativeConstraint(self.edge, self.when, self.people - self.path1.get_people())
        elif path == self.path2:
            return NegativeConstraint(self.edge, self.when, self.people - self.path2.get_people())
        else:
            raise ValueError("Not part of this Collision")

    def get_positive_constraint(self, path):
        if path == self.path1:
            return PositiveConstraint(self.edge, self.when, self.people - self.path1.get_people())
        elif path == self.path2:
            return PositiveConstraint(self.edge, self.when, self.people - self.path2.get_people())
        else:
            raise ValueError("Not part of this Collision")

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self.edge, self.when, self.people, tuple(sorted([self.path1.get_path()[0], self.path2.get_path()[0]]))))

    def __str__(self):
        return "Collision at edge %s->%s at time %d number of people %d (from %s and %s)" % (
            self.edge.from_node, self.edge.to_node, self.when, self.people, self.path1.get_path()[0], self.path2.get_path()[0])
