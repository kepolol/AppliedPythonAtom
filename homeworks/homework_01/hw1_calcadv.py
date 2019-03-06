#!/usr/bin/env python
# coding: utf-8


import re
from pyrpn import Rpn


def advanced_calculator(input_string):
    print(input_string)
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    if false_str(input_string) == None:
        return None
    try:
        return Rpn(to_polish(reformat_string(input_string))).solve()
    except IndexError:
        return None


def false_str(string):
    if len(re.findall(r'(\d+\s+\d+)|(\)+\s+\d+)|(\d+\s+\(+)|('
                      r'\)+\s+\(+)', string)):
        return None
    string = re.sub(' ', '', string)
    string = string.replace("\t", "")
    if len(re.findall("r(^[0-9, (, ), +, \-, \*, /,., \t])|("
                      "(\*\*)+)|([\[,\]])|(\,) ", string))!= 0:
        return None
    elif len(re.findall("((\(\))+)|([A-Za-z])|([=, \n])", string)) != 0:
        return None
    elif len(re.findall("[0-9]", string)) == 0:
        return None
    elif len(re.findall(re.compile(u"[А-Яа-я, ё]"), string)) != 0:
        return None
    else:
        return 1


def reformat_string(string):
    string = string.replace(" ", "")
    string = string.replace("\t", "")
    string = re.sub(r'(\-{2})+', '+', string)
    string = re.sub(r'\++', '+', string)
    string = re.sub(r'(\+\-)+', '-', string)
    string = re.sub(r'(\-\+)+', '-', string)
    string = re.sub(r'(\)|[0-9]|x)(\-)', r'\1\2 ', string)
    string = re.sub(r'([\*\/])(\-)', r'\1 \2', string)
    exp = re.findall(r'(-*[0-9,\.]+)|([*+^\/-]+|[A-Za-z]+)|(\(|\))', string)
    exp = [tuple(j for j in i if j)[-1] for i in exp]
    for i, x in enumerate(exp):
        try:
            exp[i] = float(x)
        except ValueError:
            pass
    if exp[0] in ['+', '-']:
        exp.reverse()
        exp.append(0.0)
        exp.reverse()
    return exp


def significant(i, j):
    operator = {'+': 1, '-': 1, '*': 2, '/': 2}
    try:
        a = operator[i]
        b = operator[j]
        return True if a <= b else False
    except KeyError:
        return False


def to_polish(exp):
    polish = []
    stack = []
    for i in exp:
        if type(i) is float:
            polish.append(i)
        elif i == '(':
            stack.append('(')
        elif i == ')':
            while stack and stack[-1] != '(':
                a = stack.pop()
                polish.append(a)
            if stack and stack[-1] != '(':
                return -1
            else:
                stack.pop()
        else:
            while stack and significant(i, stack[-1]):
                polish.append(stack.pop())
            stack.append(i)
    while stack:
        polish.append(stack.pop())
    return " ".join([str(i) for i in polish])
