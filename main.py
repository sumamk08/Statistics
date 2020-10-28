#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the getSequenceSum function below.
def getSequenceSum(i, j, k):
    # sum = 0
    # for x in range(i,j+1):
    #     sum= sum + x
    #
    # x = j - 1
    # while(x >= k):
    #     sum = sum + x
    #     x = x - 1
    # return sum

    list = [*range(i,j+1)]
    sum = 0
    for x in list:
        print(x)
        sum = sum + x

    x = j - 1
    list = [*range(x, k-1, -1)]
    for x in list:
        print(x)
        sum = sum + x

    # while(x >= k):
    #     sum = sum + x
    #     x = x - 1
    return sum
if __name__ == '__main__':
    print(getSequenceSum(5, 9, 6))