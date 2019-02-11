#!/bin/python3

"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem
"""

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # sum of first n natural number squared - sum of square of first n natural number
    diff = (n*(n+1)/2)**2 - ((n**3)/3 + (n**2)/2 + (n/6))
    print(int(diff))
