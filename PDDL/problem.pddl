(define (problem enmergency) (:domain exit)

(:objects
    agent1 agent2 - object
    a b c d e - block
)

(:init
    (adjacent a b) (= (road-length a b) 6)
    (adjacent b a) (= (road-length a b) 6)

    (adjacent a d) (= (road-length a d) 1)
    (adjacent d a) (= (road-length a d) 1)

    (adjacent b d) (= (road-length b d) 2)
    (adjacent d b) (= (road-length b d) 2)

    (adjacent b e) (= (road-length b e) 2)
    (adjacent e b) (= (road-length b e) 2)

    (adjacent b c) (= (road-length b c) 5)
    (adjacent c b) (= (road-length b c) 5)

    (adjacent c e) (= (road-length c e) 5)
    (adjacent e c) (= (road-length c e) 5)

    (adjacent d e) (= (road-length d e) 1)
    (adjacent e d) (= (road-length d e) 1)

    (at agent1 a)
    (at agent2 a)
    
    (= (total-cost) 0)
)

(:goal (and
        (at agent1 e)
        (at agent2 e)
    )
)

(:metric minimize (total-cost))

)
