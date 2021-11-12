(define (problem enmergency) (:domain exit)

(:objects
    a b c d e - nodes
    agent1 agent2 agent3 - people
)

(:init
    (available agent1)

    (next-agent agent1 agent2)
    (next-agent agent2 agent3)
    (next-agent agent3 agent1)      
    (last-agent agent3)


    (exit e)
    (exit c)
    
    (adjacent a b) (adjacent b a)
    (adjacent a d) (adjacent d a)
    (adjacent b d) (adjacent d b) 
    (adjacent b e) (adjacent e b)
    (adjacent b c) (adjacent c b) 
    (adjacent c e) (adjacent e c)
    (adjacent d e) (adjacent e d)

    (adjacent a a)
    (adjacent b b)
    (adjacent c c)
    (adjacent d d) 
    (adjacent e e)

    (= (road_cost) 0)

    (= (road_risk a b) 6)
    (= (road_risk a d) 1)
    (= (road_risk b d) 2)
    (= (road_risk b e) 2)
    (= (road_risk b c) 5)
    (= (road_risk c e) 5)
    (= (road_risk d e) 6)

    (= (road_crowd a b ) 1)
    (= (road_crowd a d) 1)
    (= (road_crowd b d) 1)
    (= (road_crowd b e) 1)
    (= (road_crowd b c) 1)
    (= (road_crowd c e) 1)
    (= (road_crowd d e) 1)

    (at_node agent1 a)
    (at_node agent2 a)
    (at_node agent3 a)
)

(:goal (and
    (at-exit agent1)
    (at-exit agent2)
    (at-exit agent3)
))
(:metric minimize (road_cost))
)