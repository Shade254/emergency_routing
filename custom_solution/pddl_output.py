import getopt
import sys

from graph import *


def output_to_pddl(graph, path="problem.pddl"):
    pddl_string = "(define (problem emergency) (:domain exit)\n"
    pddl_string += "(:objects\n"

    all_nodes = graph.get_all_nodes()
    all_edges = graph.get_all_edges()
    people_nodes = graph.get_nodes_with_people()
    all_agents = []

    for n in all_nodes:
        pddl_string += n + " "

    pddl_string += " - nodes\n"

    for e in all_edges:
        pddl_string += e.from_node + "-" + e.to_node + " "
    for n in all_nodes:
        pddl_string += n + "-" + n + " "

    pddl_string += " - edges\n"

    for k, v in people_nodes.items():
        for i in range(v):
            agent = k + "_" + str(i)
            all_agents.append(agent)
            pddl_string += agent + " "

    pddl_string += "virtual "
    pddl_string += " - people\n"
    pddl_string += "to from - modes\n"
    pddl_string += ")\n\n"
    pddl_string += "(:init\n"

    pddl_string += "(= (road_cost) 0)(mode from)(to-mode to)(from-mode from)(available virtual)(last-agent virtual)"
    pddl_string += "\n (first-agent %s)" % all_agents[0]

    pddl_string += "\n"

    for i in all_edges:
        pddl_string += "(= (counter %s-%s) 0)\n" % (i.from_node, i.to_node)
    for i in all_nodes:
        pddl_string += "(= (counter %s-%s) 0)\n" % (i, i)

    for i in range(len(all_agents)):
        first = all_agents[i]
        if i == len(all_agents) - 1:
            second = "virtual"
        else:
            second = all_agents[i + 1]

        pddl_string += "\n (next-agent %s %s)" % (first, second)

    pddl_string += "\n"

    for i in all_nodes:
        pddl_string += "(entry %s %s-%s)(leave %s-%s %s)\n" % (i, i, i, i, i, i)

    for i in all_edges:
        pddl_string += "(entry %s %s-%s)(leave %s-%s %s)\n" % (i.from_node, i.from_node, i.to_node, i.from_node, i.to_node, i.to_node)

    for i in all_edges:
        if not isinstance(i.risk, ConstantFunction):
            raise ValueError("Non-constant risk in the edge " + i)
        pddl_string += "(= (road_risk %s-%s) %d)\n" % (i.from_node, i.to_node, i.risk.get_risk(0))

    for i in all_nodes:
        n = graph.get_node(i)
        if not isinstance(n.risk, ConstantFunction):
            raise ValueError("Non-constant risk in the node " + n)
        pddl_string += "(= (road_risk %s-%s) %d)\n" % (i, i, n.risk.get_risk(0))

    for k, v in people_nodes.items():
        for i in range(v):
            agent = k + "_" + str(i)
            pddl_string += "(at_node %s %s)\n" % (agent, k)

    for n in all_nodes:
        if graph.get_node(n).is_exit:
            pddl_string += "(exit %s)\n" % n

    pddl_string += ")"

    pddl_string += "\n\n"
    pddl_string += "(:goal (and\n"

    for a in all_agents:
        pddl_string += "(at-exit %s)\n" % a

    pddl_string += "(forall (?e - edges) (= (counter ?e) 0))))\n\n"
    pddl_string += "(:metric minimize (road_cost)))"

    with open(path, "w") as file:
        file.write(pddl_string)


if __name__ == "__main__":
    input_file = None
    output_file = None

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "i:o:")
    except:
        print("Cannot load input arguments")
        sys.exit(1)

    for opt, arg in opts:
        if opt in ['-i']:
            input_file = arg
        elif opt in ['-o']:
            output_file = arg

    if not input_file:
        print("Cannot load input arguments")
        sys.exit(1)

    if not output_file:
        output_file = input_file.split("/")[-1].split(".")[-2] + ".pddl"

    graph = Graph(input_file)
    output_to_pddl(graph, output_file)
