#!/bin/python3

"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem
"""

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 1
    j = 1
    k = 0
    sum = 0
    while(k < n):
        k = i + j
        i = j
        j = k
        if(k < n and k%2 == 0):
            sum = sum + k
    print(sum)
