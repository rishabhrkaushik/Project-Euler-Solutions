#!/bin/python3

"""
    Author: Rishabh Kaushik
    e-mail: rishabhrkaushik@gmail.com
    website: https://rishabhrkaushik.github.io
    Purpose: This is part of the series to the solution to Project Euler.
    Problem Statement: https://www.hackerrank.com/contests/projecteuler/challenges/euler013/problem
"""

import sys
t = int(input().strip())
sum = 0
for a0 in range(t):
    n = int(input().strip())
    sum = sum + n 
print(int(str(sum)[0:10]))
