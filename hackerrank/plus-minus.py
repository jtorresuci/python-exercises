#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    size = len(arr)
    pos_neg_zero = [0] * 3
    for num in arr:
        if num > 0:
            pos_neg_zero[0] += 1
        elif num < 0:
            pos_neg_zero[1] += 1
        else:
            pos_neg_zero[2] += 1
    print("%.6f" % (pos_neg_zero[0] / size))
    print("%.6f" % (pos_neg_zero[1] / size))
    print("%.6f" % (pos_neg_zero[2] / size))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
