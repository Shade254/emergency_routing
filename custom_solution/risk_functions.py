class RiskFunction:
    def get_risk(self, people):
        pass


class ConstantFunction(RiskFunction):
    def __init__(self, constant):

        # edge costs should be non zero
        if constant == 0:
            constant = 1

        self.constant = constant

    def get_risk(self, people):
        return self.constant

    def __str__(self):
        return "{ConstantFunction risk=%d}" % self.constant


class CapacityFunction(RiskFunction):
    def __init__(self, capacity):
        self.capacity = {}
        for key in capacity:

            # edge costs should be non zero
            if capacity[key] == 0:
                self.capacity[int(key)] = 1
            else:
                self.capacity[int(key)] = capacity[key]

    def get_risk(self, people):
        for key, value in self.capacity.items():
            if people < key:
                return value

        # cannot send that many people through the corridor
        return None

    def __str__(self):
        str = "{CapacityFunction["
        for key in self.capacity:
            str += "%d->%d, " % (key, self.capacity[key])
        str = str[:-2]
        str += "]}"
        return str
