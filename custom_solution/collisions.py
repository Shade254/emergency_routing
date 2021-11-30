
def merge_collision(collisions):
    merged_collisions = []
    for i in range(len(collisions)):
        current_collision = collisions[i]
        collisions_to_merge = []

        already_merged = False
        for m in merged_collisions:
            if m.can_merge(current_collision):
                already_merged = True

        if already_merged:
            continue

        for j in range(i, len(collisions)):
            if i != j:
                if collisions[i].can_merge(collisions[j]):
                    collisions_to_merge.append(collisions[j])

        for c in collisions_to_merge:
            current_collision.merge(c)

        merged_collisions.append(current_collision)
    return merged_collisions

#added graph input to get it to run 
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
                                collisions.append(Collision(shortest_paths[i], shortest_paths[j], graph.get_edge(path1[x], path1[x + 1]), timing1[x]))

    return collisions

class Constraint():
    
    def __init__(self, edge, when, people):
        self.edge = edge
        self.when = when
        self.people = people 
        

    def return_people(self): 
        return self.people


class Collision:
    def __init__(self, path1, path2, edge, when):
        self.edge = edge
        self.when = when
        self.paths = {path1, path2}
        self.constraints = []

    def can_merge(self, collision):
        return self.edge == collision.edge and self.when == collision.when

    def merge(self, collision):
        if self.can_merge(collision):
            self.paths = self.paths.union(collision.paths)
    
    def get_constraint(self, path): 
        #scuffed way of doing it with counter maybe 
        counter = 0
        sum_of_people = 0

        for i in self.paths:
            if counter != path: 
                sum_of_people += i.get_people()
            counter += 1

        #not sure if a list of constraints should be in the collision class, but made it in case
        constraint = Constraint(self.edge, self.when, sum_of_people)
        self.constraints.append(constraint)

        return constraint

    def get_all_constraints(self): 
        return self.constraints

    def __str__(self):
        return "Collision at edge %s at time %d number of paths %d" % (self.edge, self.when, len(self.paths))
