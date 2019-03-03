#!/usr/bin/env python
# coding: utf-8

import os

from utils.file_processors import PickleFileProcessor

from homeworks.homework_01.hw1_calculator import calculator
from homeworks.homework_01.hw1_calcadv import advanced_calculator
from homeworks.homework_01.hw1_brseq import is_bracket_correct
from homeworks.homework_01.hw1_arrsearch import find_indices
from homeworks.homework_01.hw1_invertint import reverse
from homeworks.homework_01.hw1_palindrom import check_palindrom
from homeworks.homework_01.hw1_invertdict import invert_dict
from homeworks.homework_01.hw1_det import calculate_determinant


def load_test_data(func_name):
    file_processor = PickleFileProcessor()
    test_filename = os.path.basename(__file__)
    test_filename = os.path.splitext(test_filename)[0]
    test_filename = os.path.join("tests/tests_data/test_hw_01_" + func_name + ".ini.pkl")
    output = file_processor.read_file(test_filename)
    return output
data = load_test_data("calcadv")
with open('polish_answer.txt', 'w', encoding='utf-8') as g:
    for val in data:
        g.write("%s\n" %str(val))
