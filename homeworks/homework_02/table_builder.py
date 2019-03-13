#!/usr/bin/env python
# coding: utf-8


from other_methods import columns_len


def table_builder(data):
    col_len = columns_len(data)
    hyphens = '-' * (sum(col_len) + 4 * len(data[0]) + 5)
    print(hyphens)
    for lists in data[:1]:
        print(''.join(['|', (int((col_len[0] - len(
            str(lists[0])) + 1) / 2) + 2) * ' ', str(
            lists[0]), (int((col_len[0] - len(
                str(lists[0]))) / 2) + 2) * ' ' +
                '|', (int((col_len[1] - len(
                    str(lists[1])) + 1) / 2) + 2) * ' ', str(
            lists[1]), (int((col_len[1] - len(
                str(lists[1])) + 1) / 2) + 2) * ' ' +
                '|', (int((col_len[2] - len(
                    str(lists[2])) + 1) / 2) + 2) * ' ', str(
            lists[2]), (int((col_len[2] - len(
                str(lists[2])) + 1) / 2) + 2) * ' ' +
                '|', (int((col_len[3] - len(
                    str(lists[3])) + 1) / 2) + 2) * ' ', str(
            lists[3]), (int((col_len[3] - len(
                str(lists[3])) + 1) / 2) + 2) * ' ' + '|']))
    for lists in data[1:]:
        print(''.join(['|', 2 * ' ', str(lists[0]), (
                col_len[0] - len(str(lists[0])) + 2) * ' ' +
                '|', 2 * ' ', str(lists[1]), (
                col_len[1] - len(str(lists[1])) + 2) * ' ' +
                '|', 2 * ' ', str(lists[2]), (
                col_len[2] - len(str(lists[2])) + 2) * ' ' +
                '|', (col_len[3] - len(str(
                    lists[3])) + 2) * ' ', str(lists[3]), 2 * ' ' + '|']))
    print(hyphens)
