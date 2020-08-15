from inspect import signature

def bool_sat(f):
    args = len(signature(f).parameters)
    max = 2 ** args
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
