#!/usr/bin/python3

def roman_to_int(roman_string):
    string = roman_string.upper()
    dic = {
            'I': 1,
            'II': 2,
            'III': 3,
            'IV': 4,
            'V': 5,
            'VI': 6,
            'VII': 7,
            'VIII': 8,
            'IX': 9,
            'X': 10,
            'XX': 20,
            'XXX': 30,
            'XL': 40,
            'L': 50,
            'LX': 60,
            'LXX': 70,
            'LXXX': 80,
            'XC': 90,
            'C': 100,
            'CC': 200,
            'CCC': 300,
            'CD': 400,
            'D': 500,
            'DC': 600,
            'DCC': 700,
            'DCCC': 800,
            'CM': 900,
            'M': 1000,
            'MM': 2000,
            'MMM': 3000,
           }

    sum = 0
    for char in string:
        if char not in dic:
            return 0
        else:
            sum += dic[char]
    if 'IV' in string:
        sum -= 2
    if 'IX' in string:
        sum -= 2
    if 'XL' in string:
        sum -= 20
    if 'XC' in string:
        sum -= 20
    if 'CD' in string:
        sum -= 200
    if 'CM' in string:
        sum -= 200
    return sum
