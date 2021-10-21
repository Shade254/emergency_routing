(define (domain exit)

(:requirements :typing :action-costs)

(:types object block)
(:predicates
    (adjacent ?from - block ?to - block)
    (at ?agent - object ?from - block)
)

(:functions
    (road-length ?from ?to - block) - number
    (total-cost) - number
)

(:action move
    :parameters (?agent - object ?from - block ?to - block)
    :precondition (and 
        (at ?agent ?from)
        (adjacent ?from ?to)

    )
    :effect (and 
        (not (at ?agent ?from))
        (at ?agent ?to)
        (increase (total-cost) (road-length ?from ?to))
    )
    )
)
