#!/bin/python3


import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    counter = 0
    i = 0
    # 0 0 1 0 0 1 0


    while i < len(c)-1:
        if i+2 <= len(c)-1 and c[i+2]==0:
            i = i+2
            #counter += 1
        else:
            i += 1
            #counter += 1
        counter += 1    
    return(counter)
        
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')


    n = int(input())


    c = list(map(int, input().rstrip().split()))


    result = jumpingOnClouds(c)


    fptr.write(str(result) + '\n')


    fptr.close()
 












