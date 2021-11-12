(define (domain exit)

(:requirements :typing :negative-preconditions)

(:types people nodes modes edges)

(:predicates
    (available ?agent - people)
    (entry ?from - nodes ?to - edges)
    (leave ?from - edges ?to - nodes)
    (at_node ?agent - people ?at - nodes)
    (at_edge ?agent - people ?at - edges)
    (next-agent ?agent - people ?nagent - people)
    (last-agent ?agent - people)
    (first-agent ?agent - people)
    (exit ?from - nodes)
    (at-exit ?agent - people)
    (mode ?m - modes)
    (to-mode ?m - modes)
    (from-mode ?m - modes)
)

(:functions
    (road_crowd ?from - nodes ?to - nodes) - number
    (road_risk ?through - edges) - number
    (road_cost) - number
    (counter ?through - edges) - number
)

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
    :parameters (?agent - people ?from - nodes)
    :precondition (and
        (available ?agent)
        (at_node ?agent ?from)
        (exit ?from)
        (not (at-exit ?agent))
    )
    :effect (and
        (not (at_node ?agent ?from))
        (at-exit ?agent)
    ))

(:action end-of-round
    :parameters (?agent - people ?nagent - people ?m1 - modes ?m2 - modes)
    :precondition (and
        (available ?agent)
        (last-agent ?agent)
        (first-agent ?nagent)
        (mode ?m1)
        (not (mode ?m2))
    )
    :effect (and
        (not (available ?agent))
        (available ?nagent)
        (mode ?m2)
        (not (mode ?m1))
    ))


(:action move-to-edge
    :parameters (?agent - people ?from - nodes ?to - edges ?nagent - people ?m - modes)
    :precondition (and
        (available ?agent)
        (at_node ?agent ?from)
        (entry ?from ?to)
        (next-agent ?agent ?nagent)
        (not (at-exit ?agent))
        (mode ?m)
        (to-mode ?m)
        (not (last-agent ?agent))
    )
    :effect (and
        (not (at_node ?agent ?from))
        (at_edge ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (assign (road_cost) (road_risk ?to))
        (assign (counter ?to) 1)
    ))

(:action move-from-edge
    :parameters (?agent - people ?from - edges ?to - nodes ?nagent - people ?m - modes)
    :precondition (and
        (available ?agent)
        (at_edge ?agent ?from)
        (leave ?from ?to)
        (next-agent ?agent ?nagent)
        (not (at-exit ?agent))
        (mode ?m)
        (from-mode ?m)
        (not (last-agent ?agent))
    )
    :effect (and
        (not (at_edge ?agent ?from))
        (at_node ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (assign (counter ?from) -1)
    ))
)
)



