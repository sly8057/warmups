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
    positivos, negativos, zeros = 0, 0, 0
    assert 0 < len(arr) <= 100, "Insuficiencia de indices"
    for index, numeros in enumerate(arr):
        assert -100 <= numeros <= 100, f"[{index}] = {numeros} fuera de rango"
        if(numeros == 0):
            zeros += 1
        elif(numeros < 0):
            negativos += 1
        else:
            positivos += 1
    print(f"{(positivos/len(arr)):.6f}")
    print(f"{(negativos/len(arr)):.6f}")
    print(f"{(zeros/len(arr)):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
