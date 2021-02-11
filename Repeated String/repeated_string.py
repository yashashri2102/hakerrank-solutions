#!/bin/python3
 
import math
import os
import random
import re
import sys
 
# Complete the repeatedString function below.
#cfimaakj
#554045874191
#ExpectedOutput
#138511468548
def repeatedString(s, n):
    # Failing for memory error
    # counter = 0
    # if len(s) == 1 and s == 'a':
    #     counter = len(s)*n
    #     #return counter
    # else:
    #     remaining_characters = n%len(s)
    #     final_string = s*int(n/len(s))
    #     if remaining_characters:
    #         final_string += s[:remaining_characters]
    #     for f in final_string:
    #         if f == 'a':
    #             counter += 1
    # return counter
    counter = 0
    multiplier = int(n/len(s))
    no_of_a = 0
    for i in s:
        if i == "a":
            no_of_a += 1
    counter = multiplier * no_of_a
    remaining_characters = n%len(s)
    if remaining_characters:
        for f in s[:remaining_characters]:
            if f == 'a':
                counter += 1
    return counter