class EdgeCostFunction:
    def get_risk(self, people, edge):
        return (edge.risk.get_risk(people) + edge.capacity.get_risk(people)) * edge.travel_time
