#Programto find depth from sea level  U-uphill  D-downhill

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude = valleys = 0
    for step in s:
        altitude += 1 if step == 'U' else -1
        if altitude == 0 and step == 'U':
            valleys += 1

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
