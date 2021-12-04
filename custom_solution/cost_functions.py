class EdgeCostFunction:
    @staticmethod
    def get_risk(people, edge):
        if not edge.risk.get_risk(people) or not edge.capacity.get_risk(people):
            return None
        base_cost = ((edge.risk.get_risk(people) + edge.capacity.get_risk(people)) * edge.travel_time)
        return base_cost
