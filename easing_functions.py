# coding=utf-8


def linear(t, b, c, d):
    function = f'{c} * {t} / {d} + {b}'
    print(function)





# 判断函数
def judge(Choose_Function, Choose_Method, t, b, c, d):
    dict_function = {
        'linear': linear

    }
    linear(t, b, c, d)

