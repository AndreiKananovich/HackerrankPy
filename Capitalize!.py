import math
import os
import random
import re
import sys


def solve(s):
    b = []
    s = s.split(" ")
    for el in s:
        el = el.capitalize()
        b.append(el)

    return " ".join(b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()