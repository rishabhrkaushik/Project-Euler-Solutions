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
  
# maximum number till where primes needs to be checked
MAXN = 100000
  
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

# list of all primes
primes = [i for i, x in enumerate(isPrime) if x == True]

# find prime factors of number
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

# save number of divisors to prevent recalculation
divisors = {}
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 2
    found = False
    while(not found):
        # nth triangle number is sum of first n natural numbers
        # using sum of AP to find the number        
        triangle = int(((i) * (i + 1))/2)
        # check if number of divisors have already been calculated        
        try:
            divisors[i]
        except:
            # find prime factors for the number
            factors = primeFactors(triangle)
            # number of divisors
            tempN = 1
            # if the prime factors of a number is a1^b1 , a2^b2 , a3^b3 ..., an ^ bn then the number of divisors is (b1 + 1)(b2 + 1)(b3 + 1)...(bn + 1)
            for unique in set(factors):
                tempN = tempN * (factors.count(unique) + 1)
            # add it to dictionary
            divisors[i] = tempN
        # check if minimum number of divisors have been matched
        if(divisors[i] > n):
            found = True
            print(triangle)
        i = i + 1

