#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    """
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    """
    if operator in ['plus', 'minus', 'mult', 'divide'] and not isinstance(x, str) \
    and not isinstance(y, str):
        print(type(x))
        try:
            if operator == 'plus':
                return x + y
            elif operator == 'minus':
                return x - y
            elif operator == 'mult':
                return x * y
            elif operator == 'divide':
                return x / y
        except ZeroDivisionError:
            return None
        except TypeError:
            return None
    else:
        return None
    raise NotImplementedError
