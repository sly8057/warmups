#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for num in range(1, n + 1):
        if(num % 3 == 0 and num % 5 != 0):
            print("Fizz")
        elif(num % 5 == 0 and num % 3 != 0):
            print("Buzz")
        elif(num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
        else:
            print(num)
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
