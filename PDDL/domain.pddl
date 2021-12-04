(define (domain exit)

(:requirements :strips :typing :negative-preconditions :fluents)

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
    (road_risk ?through - edges) - number
    (road_cost) - number
    (counter ?through - edges) - number
    (capacity-0 ?at - edges) - number
    (crowding-0 ?at - edges) - number
    (capacity-1 ?at - edges) - number
    (crowding-1 ?at - edges) - number
    (capacity-2 ?at - edges) - number
    (crowding-2 ?at - edges) - number
    (capacity-3 ?at - edges) - number
    (crowding-3 ?at - edges) - number
    (capacity-4 ?at - edges) - number
    (crowding-4 ?at - edges) - number
    (capacity-5 ?at - edges) - number
    (crowding-5 ?at - edges) - number
    (capacity-6 ?at - edges) - number
    (crowding-6 ?at - edges) - number
    (capacity-7 ?at - edges) - number
    (crowding-7 ?at - edges) - number
    (capacity-8 ?at - edges) - number
    (crowding-8 ?at - edges) - number
    (capacity-9 ?at - edges) - number
    (crowding-9 ?at - edges) - number
)

; action for agent that was already evacuated
; pass the token and dont do anything else
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

; action for agent that arrived to an exit
; remove agent from the exit and mark him as evacuated
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

; action that marks end of the to-edge round
; switch mode to moving agents from-egde, pass token to the first agent
(:action end-of-round1
    :parameters (?agent - people ?nagent - people ?m1 - modes ?m2 - modes)
    :precondition (and
        (available ?agent)
        (last-agent ?agent)
        (first-agent ?nagent)
        (mode ?m1)(to-mode ?m1)(from-mode ?m2)
        )
    :effect (and
        (not (available ?agent))
        (available ?nagent)
        (mode ?m2)
        (not (mode ?m1))
    ))

; action that marks end of the from-edge round
; switch mode to moving agents to-egde, reset counters of passing people in every edge, pass token to the first agent
(:action end-of-round2
    :parameters (?agent - people ?nagent - people ?m1 - modes ?m2 - modes)
    :precondition (and
        (available ?agent)
        (last-agent ?agent)
        (first-agent ?nagent)
        (mode ?m1)(from-mode ?m1)(to-mode ?m2)
        )
    :effect (and
                (not (available ?agent))
                (available ?nagent)
                (mode ?m2)
                (not (mode ?m1))
                (forall (?e - edges)
                   (when (> (counter ?e) 0)
                        (assign (counter ?e) 0))
                )
            )
)

; action moving single agent with token onto an edge
; agent that has the token will be removed from the node, appears on the edge, increases plan cost by edge cost,
; increases counter of passing people by 1 and passes the token to the next agent
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
        (increase (road_cost) (road_risk ?to))
        (increase (counter ?to) 1)
    ))
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; actions moving single agent with token from an edge
; agent that has the token will be removed from the edge, appears in the node, passes the token to the next agent
; and increases plan cost by a number that is derived from edge capacity function and counter of people passing the edge in this turn

(:action move-from-edge-0
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
        (< (counter ?from) (capacity-0 ?from))
    )
    :effect (and
        (not (at_edge ?agent ?from))
        (at_node ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (increase (road_cost) (crowding-0 ?from))
    ))
(:action move-from-edge-1
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
        (>= (counter ?from) (capacity-0 ?from))
        (< (counter ?from) (capacity-1 ?from))
    )
    :effect (and
        (not (at_edge ?agent ?from))
        (at_node ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (increase (road_cost) (crowding-1 ?from))
    ))
(:action move-from-edge-2
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
        (>= (counter ?from) (capacity-1 ?from))
        (< (counter ?from) (capacity-2 ?from))
    )
    :effect (and
        (not (at_edge ?agent ?from))
        (at_node ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (increase (road_cost) (crowding-2 ?from))
    ))

(:action move-from-edge-3
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
        (>= (counter ?from) (capacity-2 ?from))
        (< (counter ?from) (capacity-3 ?from))
    )
    :effect (and
        (not (at_edge ?agent ?from))
        (at_node ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (increase (road_cost) (crowding-3 ?from))
    ))

(:action move-from-edge-4
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
        (>= (counter ?from) (capacity-3 ?from))
        (< (counter ?from) (capacity-4 ?from))
    )
    :effect (and
        (not (at_edge ?agent ?from))
        (at_node ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (increase (road_cost) (crowding-4 ?from))
    ))

(:action move-from-edge-5
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
        (>= (counter ?from) (capacity-4 ?from))
        (< (counter ?from) (capacity-5 ?from))
    )
    :effect (and
        (not (at_edge ?agent ?from))
        (at_node ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (increase (road_cost) (crowding-5 ?from))
    ))
(:action move-from-edge-6
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
        (>= (counter ?from) (capacity-5 ?from))
        (< (counter ?from) (capacity-6 ?from))
    )
    :effect (and
        (not (at_edge ?agent ?from))
        (at_node ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (increase (road_cost) (crowding-6 ?from))
    ))
(:action move-from-edge-7
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
        (>= (counter ?from) (capacity-6 ?from))
        (< (counter ?from) (capacity-7 ?from))
    )
    :effect (and
        (not (at_edge ?agent ?from))
        (at_node ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (increase (road_cost) (crowding-7 ?from))
    ))
(:action move-from-edge-8
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
        (>= (counter ?from) (capacity-7 ?from))
        (< (counter ?from) (capacity-8 ?from))
    )
    :effect (and
        (not (at_edge ?agent ?from))
        (at_node ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (increase (road_cost) (crowding-8 ?from))
    ))
(:action move-from-edge-9
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
        (>= (counter ?from) (capacity-8 ?from))
        (< (counter ?from) (capacity-9 ?from))
    )
    :effect (and
        (not (at_edge ?agent ?from))
        (at_node ?agent ?to)
        (available ?nagent)
        (not (available ?agent))
        (increase (road_cost) (crowding-9 ?from))
    ))
)



