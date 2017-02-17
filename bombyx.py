##
## bombyx.py for 106bombyx in /home/arthur.melin/Code/106bombyx
##
## Made by Arthur Melin
## Login   <arthur.melin@epitech.eu>
##
## Started on  Fri Feb 10 18:32:16 2017 Arthur Melin
## Last update Sat Feb 11 15:41:20 2017 Arthur Melin
##

import sys

def bombyx(x, k):
    return k * x * (1000 - x) / 1000

def bombyx_gen(n, k, i0):
    x = float(n)
    for i in range(1, i0):
        x = bombyx(x, k)
    return (x)

def growth(args):
    try:
        n = int(args[1])
        k = float(args[2])
    except ValueError as err:
        raise Exception('error: invalid arguments') from err
    if n < 0:
        raise Exception('error: negative number of first-gen individuals')
    if not 1 <= k <= 4:
        raise Exception('error: growth rate not between 1 and 4')

    x = float(n)
    for i in range(100):
        print(i + 1, '%.2f' % x)
        x = bombyx(x, k)

    return (0)

def scheme(args):
    try:
        n = int(args[1])
        i0 = int(args[2])
        i1 = int(args[3])
    except ValueError as err:
        raise Exception('error: invalid arguments') from err
    if n < 0:
        raise Exception('error: negative number of first-gen individuals')
    if i0 < 1 or i1 < 1:
        raise Exception('error: negative generation number')
    if i0 > i1:
        raise Exception('error: initial generation after final generation')

    k = 1.00
    while k < 4.00:
        x = bombyx_gen(n, k, i0)
        for i in range(i1 - i0 + 1):
            print('%.2f' % k, '%.2f' % x)
            x = bombyx(x, k)
        k += 0.01

    return (0)

def usage(output):
    output.write('USAGE\n')
    output.write('\t./106bombyx n [k | i0 i1]\n')
    output.write('\n')
    output.write('DESCRIPTION\n')
    output.write('\tn\tnumber of first generation individuals\n')
    output.write('\tn\tgrowth rate from 1 to 4\n')
    output.write('\ti0\tinitial generation (included)\n')
    output.write('\ti1\tfinal generation (included)\n')

def main(args):
    try:
        if len(args) == 2 and args[1] == '-h':
            usage(sys.stdout)
            return (0)
        elif len(args) == 3:
            return (growth(args))
        elif len(args) == 4:
            return (scheme(args))
        else:
            usage(sys.stderr)
            return (84)
    except Exception as ex:
        print(ex.args[0], file=sys.stderr)
        return (84)
