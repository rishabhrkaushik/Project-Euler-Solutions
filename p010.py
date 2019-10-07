#!/bin/python3

"""
    Author: Rishabh Kaushik
    e-mail: rishabhrkaushik@gmail.com
    website: https://rishabhrkaushik.github.io
    Purpose: This is part of the series to the solution to Project Euler.
    Problem Statement: https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem
"""

import sys

import math
n = 1000000

# array specifying if the below index is prime or not
primes = [ True ] * n 
p = 2
# Use Sieve of Eratosthenes algorirthm to find all the primes below 10^6
# refer https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes for alogirithm
for i in range(2, int(math.sqrt(n))):
    if(primes[i]):
        for j in range(i*i, n, i):
            primes[j] = False

# calculate all the sums to directly use them while printing the sum and reduce number of operation
sums = [ 0 ] * n 
lastSum = 0            
for i in range(2, n):
    if(primes[i]):
        sums[i] = lastSum + i 
    else:
        sums[i] = lastSum
    lastSum = sums[i]
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum = 0
    print(sums[n])
