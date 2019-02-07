#!/bin/python3

"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
"""

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum = 0
    n3 = (n-1)//3
    sum3 = n3 * (6 + ((n3-1) * 3))
    n5 = (n-1)//5
    sum5 = n5 * (10 + ((n5-1) * 5))
    n15 = (n-1)//15
    sum15 = n15 * (30 + ((n15-1) * 15))
    sum = sum3 + sum5 - sum15
    print(sum//2)
