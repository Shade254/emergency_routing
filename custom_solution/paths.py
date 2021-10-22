class Path:
    def __init__(self, end_label):
        self.__reconstruct_path(end_label)

    def __reconstruct_path(self, label):
        self.__cost = label.get_cost()
        self.__path = []
        cur_label = label
        while cur_label:
            self.__path.append(cur_label.get_node())
            cur_label = label.get_predecessor()
        self.__path.reverse()

    def get_path(self):
        return self.__path

    def get_cost(self):
        return self.__cost
