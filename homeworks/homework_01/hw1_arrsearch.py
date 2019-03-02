#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    '''
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''
    answer = 0
    a = 0
    for i in input_list:
        num = n - i
        b = 0
        for j in input_list[a + 1::]:
            if j != num:
                b += 1
                continue
            else:
                answer = 1
                return tuple([a, b + a + 1])
        a += 1
    if answer == 0:
        return None
    raise NotImplementedError
