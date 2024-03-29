#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
#
#balanced parentheses in a string expression
def checkBalanced(t):
    brackets = ['()', '{}', '[]']
    while any(x in t for x in brackets):
        for br in brackets:
            t = t.replace(br, '')
    return not t

#verify string expression via checkBalanced function
def isBalanced(s) :
    return 'YES' if checkBalanced(s) else 'NO'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
