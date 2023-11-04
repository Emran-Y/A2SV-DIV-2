#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
# Write your code here

    l = [0] * (n+2)


    def _do(a,b,k):
        l[a] +=k
        l[b+1] -=k

    for o in queries:
        a,b,k = o[0],o[1],o[2]
        _do(a,b,k)

    c = 0
    x_max = 0
    for i in range(1,n+1):
        c +=l[i]
        x_max = max(c,x_max)

    return x_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
