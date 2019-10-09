#!/bin/python3

"""
    Author: Rishabh Kaushik
    e-mail: rishabhrkaushik@gmail.com
    website: https://rishabhrkaushik.github.io
    Purpose: This is part of the series to the solution to Project Euler.
    Problem Statement: https://www.hackerrank.com/contests/projecteuler/challenges/euler012/problem
"""

import sys

import math
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 2
    found = False
    while(not found):
        triangle = ((i) * (i + 1))/2
        print("triangle: ", triangle)
        tempN = 0
        for j in range(1, int(math.sqrt(triangle) + 1)):
            if(triangle % j == 0):
                print("Divisor: ", j)
                tempN = tempN + 2
                if(tempN > n):
                    print(int(triangle))
                    found = True 
                    break
        i = i + 1 
