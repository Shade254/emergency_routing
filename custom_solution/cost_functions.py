class EdgeCostFunction:
    def get_risk(self, people, edge):
        base_cost = ((edge.risk.get_risk(people) + edge.capacity.get_risk(people)) * edge.travel_time)
        # edge costs should be non zero
        return base_cost + 1
