#!/usr/bin/python3

if __name__ == '__main__':

    a = 10
    b = 5

    from calculator_1 import add, sub, mul, div

    addres = add(a, b)
    print("{} + {} = {}".format(a, b, addres))

    '''subtraction'''
    subres = sub(a, b)
    print("{} - {} = {}".format(a, b, subres))

    '''multiplication'''
    mulres = mul(a, b)
    print("{} * {} = {}".format(a, b, mulres))

    '''division'''
    divres = div(a, b)
    print("{} / {} = {}".format(a, b, int(divres)))
