#!/bin/python3

"""
    Author: Rishabh Kaushik
    e-mail: rishabhrkaushik@gmail.com
    website: https://rishabhrkaushik.github.io
    Purpose: This is part of the series to the solution to Project Euler.
    Problem Statement: https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem
"""

import sys

"""
  The code works in O(n)
"""

t = int(input().strip())for a0 in range(t):
    n = int(input().strip())
    # assign initial product as -1
    product = -1
    # a, b, c are sides of triangle
    # assuming a < b < c, the maximum value of a can be n/3 + 1
    for a in range(3, (n//3) + 1):
        # a + b + c = n
        # hence c = n - a - b 
        # a^2 + b^2 = c^2
        # putting c from equation above here
        # we get the following equation of b
        b = (n**2 - 2*a*n)//(2*n - 2*a)
        c = n - b - a
        # checking if the triplet found form a pythogorean triplet
        if a**2 + b **2 == c**2:
            # assign it to product if it is the largest
            if a*b*c > product:
                product = a*b*c
    print(product)
