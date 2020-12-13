#!/bin/python3
# See bottom for example input/output comment
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    x = 0
    i = 0
    j = 0
    output = 0
    sums = []
    while i <= 4:
        if len(sums) == 16:
                break
        print(i)
        j = 0
        print(sums)

        while j < 4:
            if len(sums) == 16:
                break
            x += (arr[i][j] + arr[i][j+1] + arr[i][j+2])
            
            x += (arr[i+1][j+1] + arr[i+2][j+1] + arr[i+2][j] + arr[i+2][j+2])
            
            sums.append(x)
            x = 0
            

            


            j+=1

        i += 1
    output = max(sums)
    print(output)
    # Ignore print statements!!
    return output





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# Example input:
"""1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0"""
# Example output:
# 19
