(define (problem emergency) (:domain exit)

(:objects
    a b e - nodes
    ab be ae - edges
    agent1 agent2 agent3 virtual - people
    to from - modes
)

(:init
    (mode from)
    (to-mode to)
    (from-mode from)
    (available virtual)

    (next-agent agent1 virtual)

    (last-agent virtual)
    (first-agent agent1)

    (exit e)

    (entry a ab) (entry a ae)
    (entry b ab) (entry b be)
    (entry e be) (entry e ae)

    (leave ab a) (leave ae a)
    (leave ab b) (leave be b)
    (leave be e) (leave ae e)

    (= (road_cost) 0)
    (= (counter ab) 0)
    (= (counter ae) 0)
    (= (counter be) 0)


    (= (road_risk ab) 1)
    (= (road_risk ae) 6)
    (= (road_risk be) 1)


    (at_node agent1 a)
)

(:goal (and
    (at-exit agent1)
    (forall (?e - edges) (= (counter ?e) 0))
))

(:metric minimize (road_cost))
)