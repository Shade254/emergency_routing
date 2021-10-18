class RiskFunction:
    def get_risk(self, people):
        pass


class ConstantFunction(RiskFunction):
    def __init__(self, constant):
        self.constant = constant

    def get_risk(self, people):
        return self.constant


class CapacityFunction(RiskFunction):
    def __init__(self, capacity):
        self.capacity = {}
        for key in capacity:
            self.capacity[int(key)] = capacity[key]

    def get_risk(self, people):
        for key, value in self.capacity:
            if people < key:
                return value

        # cannot send that many people through the corridor
        return None
