(define (problem enmergency) (:domain exit)

(:objects
    a b c d e - edges
)

(:init
    (Available agent1)

    (next-agent agent1 agent2)
    (next-agent agent2 agent3)
    (next-agent agent3 agent1)      
    (last-agent agent3)

    (destination agent1 e)
    (destination agent2 e)
    (destination agent3 e)
    
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

    (= (road-risk agent1 a a) 6)
    (= (road-risk agent2 a a) 6)
    (= (road-risk agent3 a a) 6)
    
    (= (road-crowd agent1 a a) 0)
    (= (road-crowd agent2 a a) 0)
    (= (road-crowd agent3 a a) 0)

    (= (road-risk agent1 b b) 6)
    (= (road-risk agent2 b b) 6)
    (= (road-risk agent3 b b) 6)
    
    (= (road-crowd agent1 b b) 0)
    (= (road-crowd agent2 b b) 0)
    (= (road-crowd agent3 b b) 0)

    (= (road-risk agent1 c c) 6)
    (= (road-risk agent2 c c) 6)
    (= (road-risk agent3 c c) 6)
    
    (= (road-crowd agent1 d d) 0)
    (= (road-crowd agent2 d d) 0)
    (= (road-crowd agent3 d d) 0)

    (= (road-risk agent1 e e) 6)
    (= (road-risk agent2 e e) 6)
    (= (road-risk agent3 e e) 6)
    
    (= (road-crowd agent1 e e) 0)
    (= (road-crowd agent2 e e) 0)
    (= (road-crowd agent3 e e) 0)

    (= (road-risk agent1 a b) 6)
    (= (road-risk agent2 a b) 6)
    (= (road-risk agent3 a b) 6)
    
    (= (road-crowd agent1 a b) 0)
    (= (road-crowd agent2 a b) 0)
    (= (road-crowd agent3 a b) 0)

    (= (road-risk agent1 a d) 1)
    (= (road-risk agent2 a d) 1)
    (= (road-risk agent3 a d) 1)
    
    (= (road-crowd agent1 a d) 0)
    (= (road-crowd agent2 a d) 0)
    (= (road-crowd agent3 a d) 0)

    (= (road-risk agent1 b d) 2)
    (= (road-risk agent2 b d) 2)
    (= (road-risk agent3 b d) 2)
    
    (= (road-crowd agent1 b d) 0)
    (= (road-crowd agent2 b d) 0)
    (= (road-crowd agent3 b d) 0)
    
    (= (road-risk agent1 b e) 2)
    (= (road-risk agent2 b e) 2)
    (= (road-risk agent3 b e) 2)
    
    (= (road-crowd agent1 b e) 0)
    (= (road-crowd agent2 b e) 0)
    (= (road-crowd agent3 b e) 0)

    (= (road-risk agent1 b c) 5)
    (= (road-risk agent2 b c) 5)
    (= (road-risk agent3 b c) 5)
    
    (= (road-crowd agent1 b c) 0)
    (= (road-crowd agent2 b c) 0)
    (= (road-crowd agent3 b c) 0)

    (= (road-risk agent1 c e) 5)
    (= (road-risk agent2 c e) 5)
    (= (road-risk agent3 c e) 5)
    
    (= (road-crowd agent1 c e) 0)
    (= (road-crowd agent2 c e) 0)
    (= (road-crowd agent3 c e) 0)

    (= (road-risk agent1 d e) 6)
    (= (road-risk agent2 d e) 6)
    (= (road-risk agent3 d e) 6)
    
    (= (road-crowd agent1 d e) 0)
    (= (road-crowd agent2 d e) 0)
    (= (road-crowd agent3 d e) 0)

    (= (road-cost agent1) 0)   
    (= (road-cost agent2) 0) 
    (= (road-cost agent3) 0) 
    
    (adjacent a a)
    (adjacent b b)
    (adjacent c c)
    (adjacent d d) 
    (adjacent e e)

    (at agent1 a)
    (at agent2 a)
    (at agent3 a)
)

(:goal (and
        (at agent1 e)
        (at agent2 e)
        (at agent3 e)
    )
)
)