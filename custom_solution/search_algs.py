from abc import abstractmethod

from paths import *
from goal_checkers import *
import Queue


class SearchAlgorithm:
    def __init__(self, start_labels, label_factory, goal_checker):
        self.__label_factory = label_factory
        self.__goal_checker = goal_checker
        self.__queue = Queue.PriorityQueue()

    @abstractmethod
    def __add_to_queue(self, label):
        pass

    def search(self):
        end_labels = []
        while not self.__queue.empty():
            priority, current_label = self.__queue().get()

            if self.__goal_checker.is_goal(current_label):
                end_labels.append(current_label)

            if self.__goal_checker.finish_search():
                break

            children = self.__label_factory.expand(current_label)
            for label in children:
                self.__add_to_queue(label)

        if not end_labels:
            return end_labels
        else:
            paths = []
            for label in end_labels:
                paths.append(Path(label))
            return paths
