from inspect import signature
from math import log2

def a(x, y, z):
    return x and y and z;

print(len(signature(a).parameters))

def bool_sat(f):
    args = len(signature(f).parameters)
    max = pow(2, args)
    num = 0
    all_solutions = []
    while num < max:
        i = 0
        digits = [0] * args
        n = num
        while (i < args):
            div = n // 2
            evendiv = (n-1) // 2
            digits[i] = (div != evendiv)
            i = i + 1
            n = div
        if f(*digits) == True:
            all_solutions.append(digits)
        num = num + 1
    return all_solutions

print(bool_sat(a))
