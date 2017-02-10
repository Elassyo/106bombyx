##
## bombyx.py for 106bombyx in /home/arthur.melin/Code/106bombyx
##
## Made by Arthur Melin
## Login   <arthur.melin@epitech.eu>
##
## Started on  Fri Feb 10 18:32:16 2017 Arthur Melin
## Last update Fri Feb 10 18:51:54 2017 Arthur Melin
##

import sys

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
