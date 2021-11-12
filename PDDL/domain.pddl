(define (domain exit)

(:requirements :typing :negative-preconditions)

(:types people nodes)

(:predicates
    (available ?agent - people)
    (adjacent ?from - nodes ?to - nodes)
    (at_node ?agent - people ?from - nodes)
    (next-agent ?agent - people ?nagent - people)
    (exit ?from - nodes)
    (at-exit ?agent - people)
)

(:functions
    (road_crowd ?from - nodes ?to - nodes) - number
    (road_risk ?from - nodes ?to - nodes) - number
    (road_cost) - number
)

(:action move
    :parameters (?agent - people ?from - nodes ?to - nodes ?nagent - people)
    :precondition (and
        (available ?agent)
        (at_node ?agent ?from)
        (adjacent ?from ?to)
        (next-agent ?agent ?nagent)
        (not (at-exit ?agent))
    )
    :effect (and
        (not (at_node ?agent ?from))
        (at_node ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (assign (road_cost) (+ (road_risk ?from ?to) (road_crowd ?from ?to)))
    ))

(:action pass
    :parameters (?agent - people ?nagent - people)
    :precondition (and
        (available ?agent)
        (next-agent ?agent ?nagent)
        (at-exit ?agent)
    )
    :effect (and
        (available ?nagent)
        (not (available ?agent))
            ))

(:action move-from-exit
    :parameters (?agent - people ?from - nodes ?nagent - people)
    :precondition (and
        (available ?agent)
        (at_node ?agent ?from)
        (next-agent ?agent ?nagent)
        (exit ?from)
        (not (at-exit ?agent))
    )
    :effect (and
        (not (at_node ?agent ?from))
        (available ?nagent)
        (not (available ?agent))
        (at-exit ?agent)
    ))
)

