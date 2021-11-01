class Path:
    def __init__(self, end_label):
        self._reconstruct_path(end_label)

    def _reconstruct_path(self, label):
        pass


class SimplePath(Path):
    def _reconstruct_path(self, label):
        self._cost = label.get_cost()
        self._path = []
        cur_label = label
        while cur_label:
            self._path.append(cur_label.get_node_id())
            cur_label = cur_label.get_predecessor()
        self._path.reverse()

    def get_path(self):
        return self._path

    def get_cost(self):
        return self._cost

    def __str__(self):
        return "PATH: %s, COST: %d" % (self._path, self._cost)
