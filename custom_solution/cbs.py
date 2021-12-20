import copy
import time
from dataclasses import dataclass

from custom_solution.collisions import add_bound_to_path, identify_all_collisions
from custom_solution.cost_functions import EdgeCostFunction
from custom_solution.paths import Path
from custom_solution.search_algs import ConstrainedExitDijkstra

iteration_counter = 0


def choose_collision(collisions):
    return collisions[0]


@dataclass(frozen=False)
class Result:
    iterations: int
    lower_bound: int
    upper_bound: int
    paths: [Path]

    def __str__(self):
        strrr = "COST (lower> %d, upper> %d)\n" % (self.lower_bound, self.upper_bound)
        for p in self.paths:
            strrr += "\t" + p.__str__() + "\n"
        return strrr


def get_bounds(paths):
    upper = 0
    lower = 0
    for p in paths:
        upper += p.upper_bound * p.get_people()
        lower += p.get_cost() * p.get_people()
    return lower, upper


def pick_best_result(results):
    results = [i for i in results if i]

    if not results:
        return None
    return sorted(results, key=lambda x: x.upper_bound)[0]


def bounds_met(bounds, tolerance):
    return bounds[0] * (1 + tolerance) >= bounds[1]


def search(replan_from, replan_people, paths, bounds, constraints, graph, solved_collisions, end_time, tolerance):
    global iteration_counter
    iteration_counter += 1
    print("\n\nIteration " + str(iteration_counter))

    if replan_from and replan_people:
        # replan specific path if chosen by parent node
        print("Replanning for " + replan_from)
        new_alg = ConstrainedExitDijkstra(replan_from, replan_people, graph, EdgeCostFunction(), constraints[replan_from])
        new_paths = new_alg.search()
        # fail if replanning not possible
        if not new_paths:
            print("No replanning possible - RETURN NONE")
            return None
        paths.append(new_paths[0])

    # detect collisions between all paths
    collisions = identify_all_collisions(paths, graph)

    print("Number of collisions: " + str(len(collisions)))

    paths2 = []
    for p in paths:
        # print(p.get_path())
        # p.output_geojson(p.get_path(), p.get_people(), graph, "it-%d-%s-%d.json" % (global_counter, p.get_path()[0], p.get_people()))
        paths2.append(add_bound_to_path(graph, p, collisions))

    paths = paths2

    new_bounds = get_bounds(paths)
    print("Bounds: PASSED - " + str(bounds) + " NEW - " + str(new_bounds))

    if bounds and new_bounds[0] >= bounds[1]:
        print("Lower bound too high - RETURN NONE")
        return None

    if bounds_met(new_bounds, tolerance):
        print("Bounds met - RETURN RESULT")
        return Result(iteration_counter, new_bounds[0], new_bounds[1], paths)

    if end_time and time.time() >= end_time:
        print("Time exceeded")
        return Result(iteration_counter, new_bounds[0], new_bounds[1], paths)

    collisions2 = []
    for c1 in collisions:
        add = True
        for c2 in solved_collisions:
            if c1 == c2:
                add = False
                break
        if add:
            collisions2.append(c1)
    collisions = collisions2

    # return set of paths as result if no collisions detected
    if not collisions:
        print("No (unsolved) collisions - RETURN RESULT")
        return Result(iteration_counter, new_bounds[0], new_bounds[1], paths)

    # choose specific collision to solve (in child nodes)
    to_solve = choose_collision(collisions2)

    print("Solving collision " + to_solve.__str__())

    new_solved_collisions = copy.deepcopy(solved_collisions)
    new_solved_collisions.append(to_solve)

    results = []

    pass_bounds = bounds
    if pass_bounds:
        pass_bounds = (new_bounds[0], min(new_bounds[1], bounds[1]))

    for path in to_solve.get_participants():
        new_replan_from = path.get_path()[0]
        new_replan_people = path.get_people()

        negative_constraint = to_solve.get_negative_constraint(path)

        # get all the other paths
        other_paths = []
        for p in paths:
            if p.people == path.get_people() and p.get_path() == path.get_path():
                continue
            other_paths.append(p)

        # get all the previous constraints and add a new one
        all_constraints = copy.deepcopy(constraints)
        if new_replan_from not in all_constraints:
            all_constraints[new_replan_from] = []
        all_constraints[new_replan_from].append(negative_constraint)
        result = search(new_replan_from, new_replan_people, other_paths, pass_bounds, all_constraints, graph, new_solved_collisions, end_time, tolerance)

        if pass_bounds and result:
            pass_bounds = (pass_bounds[0], min(pass_bounds[1], result.upper_bound))

        # run recursive search with path to replan and all the constraints
        results.append(result)
        if pass_bounds:
            if bounds_met(pass_bounds, tolerance):
                break
        elif result and bounds_met((result.lower_bound, result.upper_bound), tolerance):
            break

    dive_deeper = True
    if pass_bounds and bounds_met(pass_bounds):
        dive_deeper = False
    else:
        for r in results:
            if r and bounds_met((r.lower_bound, r.upper_bound), tolerance):
                dive_deeper = False

    if dive_deeper:
        all_constraints = copy.deepcopy(constraints)
        for path in to_solve.get_participants():
            positive_constraint = to_solve.get_positive_constraint(path)
            if path.get_path()[0] in all_constraints:
                all_constraints[path.get_path()[0]].append(positive_constraint)

        other_paths = copy.deepcopy(paths)
        results.append(search(None, None, other_paths, pass_bounds, all_constraints, graph, new_solved_collisions, end_time, tolerance))

    best = pick_best_result(results)

    if not best:
        return None

    best.iterations = iteration_counter
    return best
