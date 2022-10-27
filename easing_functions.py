# coding=utf-8
# 用于储存缓动函数并判断输出
function = ''


def linear(Choose_Method, t, b, c, d):
    global function
    function = f'{c} * {t} / {d} + {b}'
    print('1')
    return function


def quadratic(Choose_Method, t, b, c, d):
    global function
    if Choose_Method == 'In':
        function = f'{c}*({t}/{d})*{t}/{d}+{b}'
    if Choose_Method == 'Out':
        function = f'-{c}*({t}/{d})*({t}/{d}-2)+{b}'

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
