class Path:
    def __init__(self, end_label):
        self._reconstruct_path(end_label)

    def _reconstruct_path(self, label):
        pass


class SimplePath(Path):
    def _reconstruct_path(self, label):
        self._cost = label.get_cost()
        self.people = label.get_people()
        self._path = []
        self._timing = []
        cur_label = label
        while cur_label:
            self._path.append(cur_label.get_node_id())
            self._timing.append(cur_label.get_travel_time())
            cur_label = cur_label.get_predecessor()
        self._path.reverse()
        self._timing.reverse()

    def get_timing(self):
        return self._timing

    def get_people(self): 
        return self.people

    def get_path(self):
        return self._path

    def get_cost(self):
        return self._cost

    def __str__(self):
        return "PATH: %s, COST: %d" % (self._path, self._cost)

    def __eq__(self, other):
        return isinstance(other, SimplePath) and self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self._cost, tuple(self._timing), tuple(self._path)))
