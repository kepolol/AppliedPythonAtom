#!/usr/bin/env python
# coding: utf-8


import re


def advanced_calculator(input_string):
    """
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    """
    re.sub(' ', '', input_string)
    try:
        if not (not len(re.findall("[^0-9, (, ), +, \-, \*, /,., \t]", input_string)) and not len(
                re.findall("(\*\*)+", input_string))) or len(re.findall("\,", input_string)) != 0:
            return None
        elif len(re.findall("[0-9]", input_string)) == 0:
            return None
        else:
            return eval(input_string)
    except SyntaxError:
        return None
