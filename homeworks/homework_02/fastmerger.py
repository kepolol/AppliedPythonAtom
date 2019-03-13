#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        """
        принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        """
        heap, pos = MaxHeap([]), 0
        for el in list_of_lists:
            for val in el:
                heap.add((val, pos))
            pos += 1
        output = []
        heap.build_heap()
        try:
            while k > 0:
                answer = heap.extract_maximum()
                output.append(answer[0])
                heap.build_heap()
                k = k - 1
            return output
        except TypeError:
            return output
