#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hours = s[0:2]
    mins = s[3:5]
    secs = s[6:8]
    ampm = s[8:10]
    if int(hours) == 12 and ampm == "AM":
        hours = "00"
    elif ampm == "PM" and hours != "12":
        hours = str(int(hours) + 12)
    return hours + ":" + mins + ":" + secs
    
        
    print(hours, mins, secs, ampm)
    
    return ""

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
