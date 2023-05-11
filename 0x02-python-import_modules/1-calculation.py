#!/usr/bin/python3

if __name__ == '__main__':

    a = 10
    b = 5

    from calculator_1 import add, sub, mul, div

    addres = a + b
    print("{} + {} = {}".format(a, b, addres))

    #subtraction
    subres = a - b
    print("{} - {} = {}".format(a, b, subres))

    #multiplication
    mulres = a * b
    print("{} * {} = {}".format(a, b, mulres))

    #division
    divres = a / b
    print("{} / {} = {}".format(a, b, int(divres)))
