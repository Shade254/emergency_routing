(define (domain exit)

(:requirements :typing :negative-preconditions :action-costs)

(:types people edges)

(:predicates
    (Available ?agent - people)
    (adjacent ?from - edges ?to - edges)
    (at ?agent - people ?from - edges)
    (next-agent ?agent - people ?nagent - people)
    (destination ?agent - people ?from - edges)
    (last-agent ?agent - people)
    (road-risk ?agent - people ?from - edges ?to - edges)
    (road-crowd ?agent - people ?from - edges ?to - edges)
    (road-cost ?agent)
)

(:constants
    agent1 agent2 agent3 - people
)

(:functions
    (road-crowd ?agent - people ?from - edges ?to - edges) - number
    (road-risk ?agent - people ?from - edges ?to - edges) - number
    (road-cost ?agent) - number
)

(:action move
    :parameters (?agent - people ?from - edges ?to - edges ?nagent - people)
    :precondition (and 
        (not (last-agent ?agent))
        (Available ?agent)
        (at ?agent ?from)
        (adjacent ?from ?to)
        (next-agent ?agent ?nagent)
        (not (destination ?agent ?from))
    )
    :effect (and 
        (not (at ?agent ?from))
        (at ?agent ?to)
        (Available ?nagent)
        (not (Available ?agent))
        (increase (road-crowd ?agent ?from ?to) 1)
        (increase (road-cost ?agent) (road-risk ?agent ?from ?to))             
    ))

(:action init
    :parameters (?agent - people ?from - edges ?to - edges ?nagent - people)
    :precondition (and  
        (last-agent ?agent)
        (Available ?agent)
        (at ?agent ?from)
        (adjacent ?from ?to)       
        (next-agent ?agent ?nagent)
        (not (destination ?agent ?from))
    )
    :effect (and 
        (not (at ?agent ?from))
        (at ?agent ?to)
        (next-agent ?agent ?nagent)
        (not (Available ?agent))
        (Available ?nagent)
        (increase (road-crowd ?agent ?from ?to) 1)
        (increase (road-cost ?agent) (road-risk ?agent ?from ?to))   
        (decrease (road-cost ?agent) (road-crowd ?agent ?from ?to)) 
        (decrease (road-cost ?agent) (road-cost ?agent)) 
    ))
)

