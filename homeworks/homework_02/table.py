#!/usr/bin/env python
# coding: utf-8


import sys
from homeworks.homework_02.other_methods import json2lists
from homeworks.homework_02.read_data import read_json_data
from homeworks.homework_02.table_builder import table_builder

# Ваши импорты

if __name__ == '__main__':
    filename = sys.argv[1]

    # Ваш код
try:
    data = read_json_data(filename, def_enc_method(filename))
except FileNotFoundError:
    print('Файл не валиден')
if data[1] == 1:
    table_builder(data[0])
else:
    table_builder(json2lists(data[0]))
