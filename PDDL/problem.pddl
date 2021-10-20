(define (problem enmergency) (:domain exit)

(:objects
    agent1
    a b c d e - block
)

(:init
    (clear a)(clear b)(clear c)(clear d)(clear e)
    (at agent1 a)
    (adjacent a b)(adjacent a d)   
    (adjacent b d)(adjacent b e)(adjacent b c)
    (adjacent c e)
    (adjacent d e)
)

(:goal (and
        (at agent1 e)
    )
)
)
