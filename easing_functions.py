# coding=utf-8
# 用于储存缓动函数并判断输出
import math

function = ''   # 此变量的值为达芬奇fusion表达式格式
function_py = ''    # 此表达式值为python np格式


def linear(Choose_Method, t, b, c, d):
    # 线性
    global function
    function = f'{c} * {t} / {d} + {b}'
    print('1')
    return function


def quadratic(Choose_Method, t, b, c, d):
    # 二次渐变
    global function
    if Choose_Method == 'In':
        function = f'{c}*({t}/{d})*{t}/{d}+{b}'
    elif Choose_Method == 'Out':
        function = f'-{c}*({t}/{d})*({t}/{d}-2)+{b}'
    return function

def sinusoidal(Choose_Method, t, b, c, d):
    # 正弦渐变
    global function
    if Choose_Method == 'In':
        function = f"-{c} * cos({t} / {d} * (pi / 2)) + {c} + {b}"
    elif Choose_Method == 'Out':
        function = f"{c} * sin({t} / {d} * (pi / 2)) + {b}"
    return function


# 判断函数
def judge(Choose_Function, Choose_Method, t, b, c, d):
    global function
    dict_function = {
        'linear': linear,
        'quadratic': quadratic,
    }
    function = dict_function[Choose_Function](Choose_Method, t, b, c, d)
    return function
