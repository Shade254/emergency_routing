(define (domain exit)

(:requirements :typing :negative-preconditions :action-costs)

(:types people nodes)

(:predicates
    (Available ?agent - people)
    (adjacent ?from - nodes ?to - nodes)
    (at_site ?agent - people ?from - nodes)
    (next-agent ?agent - people ?nagent - people)
    (destination ?agent - people ?from - nodes)
    (last-agent ?agent - people)
)

(:functions
    (road_crowd ?from - nodes ?to - nodes) - number
    (road_risk ?from - nodes ?to - nodes) - number
    (road_cost ?agent - people) - number
)

(:action move
    :parameters (?agent - people ?from - nodes ?to - nodes ?nagent - people)
    :precondition (and 
        (not (last-agent ?agent))
        (Available ?agent)
        (at_site ?agent ?from)
        (adjacent ?from ?to)
        (next-agent ?agent ?nagent)
        (not (destination ?agent ?from))
    )
    :effect (and 
        (not (at_site ?agent ?from))
        (at_site ?agent ?to)
        (Available ?nagent)
        (not (Available ?agent))
        (assign (road_cost ?agent) (+ (road_risk ?from ?to) (road_crowd ?from ?to)))           
    ))

(:action init
    :parameters (?agent - people ?from - nodes ?to - nodes ?nagent - people)
    :precondition (and  
        (last-agent ?agent)
        (Available ?agent)
        (at_site ?agent ?from)
        (adjacent ?from ?to)       
        (next-agent ?agent ?nagent)
        (not (destination ?agent ?from))
    )
    :effect (and 
        (not (at_site ?agent ?from))
        (at_site ?agent ?to)
        (next-agent ?agent ?nagent)
        (not (Available ?agent))
        (Available ?nagent)
        (assign (road_cost ?agent) (+ (road_risk ?from ?to) (road_crowd ?from ?to)))  
    ))
)

