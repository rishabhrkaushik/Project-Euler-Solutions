#!/bin/python3

"""
    Author: Rishabh Kaushik
    e-mail: rishabhrkaushik@gmail.com
    website: https://rishabhrkaushik.github.io
    Purpose: This is part of the series to the solution to Project Euler.
    Problem Statement: https://www.hackerrank.com/contests/projecteuler/challenges/euler012/problem
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
  
MAXN = 1000000
  
# array specifying if the below index is prime or not
isPrime = [ True ] * MAXN
p = 2
# Use Sieve of Eratosthenes algorirthm to find all the primes below 10^6
# refer https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes for alogirithm
for i in range(2, int(math.sqrt(MAXN))):
    if(isPrime[i]):
        for j in range(i*i, MAXN, i):
            isPrime[j] = False
isPrime[0] = False
isPrime[1] = False

primes = [i for i, x in enumerate(isPrime) if x == True]
# print(primes)

# A O(log n) function returning prime  
# factorization by dividing by smallest  
# prime factor at every step 
def primeFactors(x): 
    factors = []
    i = 0
    while(x != 1):
        if(x % primes[i] == 0):
            factors.append(primes[i])
            x = x // primes[i]
        else:
            i = i + 1
    return factors

# print(primeFactors(100))

# n = 4
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 2
    found = False
    while(not found):
        triangle = int(((i) * (i + 1))/2)
    #     print("Triangle: ", triangle)
        factors = primeFactors(triangle)
    #     print(factors)
        tempN = 1
        for unique in set(factors):
            tempN = tempN * (factors.count(unique) + 1)
    #     print(tempN)
        if(tempN > n):
            found = True
            print(triangle)
        i = i + 1
