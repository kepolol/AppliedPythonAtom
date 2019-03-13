#!/usr/bin/env python
# coding: utf-8


class Heap:

    def __init__(self, array):
        self.array = array[::]
        self.build_heap()

    def add(self, elem_with_priority):
        """
        Метод добавления элемента в кучу.
        :param elem_with_priority:
        :return:
        """
        self.array.append(elem_with_priority)
        self.sift_up(len(self.array) - 1)

    def build_heap(self):
        """
        Метод реструктурирует кучу.
        :return:
        """
        for idx in reversed(range(int(len(self.array) / 2))):
            self.sift_down(idx)

    def sift_down(self, idx):
        """
        Метод реализует Sift Down.
        :param idx:
        :return:
        """
        left, right = 2 * idx + 1, 2 * idx + 2
        largest = idx
        if left < len(self.array) and comparator_d(
                self.array[left], self.array[largest]):
            largest = left
        if right < len(self.array) and comparator_d(
                self.array[right], self.array[largest]):
            largest = right
        if largest != idx:
            self.array[idx], self.array[largest] = \
                self.array[largest], self.array[idx]
            self.sift_down(largest)

    def sift_up(self, idx):
        """
        Метод реализует Sift Up.
        :param idx:
        :return:
        """
        while idx > 1:
            parent = int((idx - 1) / 2)
            if comparator_d(self.array[parent], self.array[idx]):
                break
            self.array[idx], self.array[parent] = \
                self.array[parent], self.array[idx]
            idx = parent


class MaxHeap(Heap):

    def __init__(self, array):
        super().__init__(array)

    def extract_maximum(self):
        """
        Метод реализует извлечение максимального элемента
        (корня дерева) из кучи.
        :return:
        """
        if len(self.array) != 0:
            output = self.array.pop(0)
            self.build_heap()
            return output


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
