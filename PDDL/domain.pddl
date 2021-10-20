(define (domain exit)

(:requirements :typing :strips :equality)

(:types object block)
(:predicates
    (at ?agent - object ?from - block)
    (adjacent ?from - block ?to - block)
    (clear ?to)
)

(:action move
    :parameters (?agent - object ?from ?to)
    :precondition (and 
        (at ?agent ?from)
        (adjacent ?from ?to)
        (clear ?to)
        
    )
    :effect (and 
        (not (at ?agent ?from))
        (at ?agent ?to)
    )
    )
)
