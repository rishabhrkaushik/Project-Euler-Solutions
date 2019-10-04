#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    product = -1
    for a in range(1, int(n/2)):
        b = (((n ** 2) - (2 * a * n))/(2 * (n - a)))
        c = n - a - b
        if((a ** 2) + (b ** 2) == (c ** 2)):
            product = int(a * b * c)
    print(product)
