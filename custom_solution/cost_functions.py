class EdgeCostFunction:
    def get_risk(self, people, edge):
        if edge.risk.get_risk(people) == None or edge.capacity.get_risk(people) == None:
            return None
        base_cost = ((edge.risk.get_risk(people) + edge.capacity.get_risk(people)) * edge.travel_time)
        # edge costs should be non zero
        return base_cost + 1
