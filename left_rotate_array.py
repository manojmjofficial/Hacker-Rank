#Program to left rotate an array

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a,k):
    alist = list(a)
    b = alist[k:]+alist[:k]
    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
