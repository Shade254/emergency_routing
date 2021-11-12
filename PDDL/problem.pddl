(define (problem emergency) (:domain exit)

(:objects
    a b c d e - nodes
    aa ab ad bb bc bd be cc ce dd de ee - edges
    agent1 agent2 agent3 virtual - people
    to from - modes
)

(:init
    (mode from)
    (to-mode to)
    (from-mode from)
    (available virtual)

    (next-agent agent1 agent2)
    (next-agent agent2 agent3)
    (next-agent agent3 virtual)

    (last-agent virtual)
    (first-agent agent1)

    (exit e)

    (entry a aa) (entry a ab) (entry a ad)
    (entry b bb) (entry b ab) (entry b bc) (entry b bd) (entry b be)
    (entry c cc) (entry c bc) (entry c ce)
    (entry d dd) (entry d ad) (entry d bd) (entry d de)
    (entry e ee) (entry e be) (entry e ce) (entry e de)

    (leave aa a) (leave ab a) (leave ad a)
    (leave bb b) (leave ab b) (leave bc b) (leave bd b) (leave be b)
    (leave cc c) (leave bc c) (leave ce c)
    (leave dd d) (leave ad d) (leave bd d) (leave de d)
    (leave ee e) (leave be e) (leave ce e) (leave de e)

    (= (road_cost) 0)
    (= (counter aa) 0)
    (= (counter ab) 0)
    (= (counter ad) 0)

    (= (counter bb) 0)
    (= (counter bc) 0)
    (= (counter bd) 0)
    (= (counter be) 0)

    (= (counter cc) 0)
    (= (counter ce) 0)

    (= (counter dd) 0)
    (= (counter de) 0)

    (= (counter ee) 0)

    (= (road_risk ab) 6)
    (= (road_risk ad) 1)
    (= (road_risk bc) 5)
    (= (road_risk bd) 2)
    (= (road_risk be) 2)
    (= (road_risk ce) 5)
    (= (road_risk de) 6)

    (= (road_risk aa) 0)
    (= (road_risk bb) 0)
    (= (road_risk cc) 0)
    (= (road_risk dd) 0)
    (= (road_risk ee) 0)

    (at_node agent1 a)
    (at_node agent2 b)
    (at_node agent3 c)
)

(:goal (and
    (at-exit agent1)
    (at-exit agent2)
    (at-exit agent3)
))
(:metric minimize (road_cost))
)