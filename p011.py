#!/bin/python3

"""
    Author: Rishabh Kaushik
    e-mail: rishabhrkaushik@gmail.com
    website: https://rishabhrkaushik.github.io
    Purpose: This is part of the series to the solution to Project Euler.
    Problem Statement: https://www.hackerrank.com/contests/projecteuler/challenges/euler011/problem
"""

import sys


grid = []
products = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)
    
for row in range(20):
    for column in range(20):
        tempProducts = [] 
        tempProducts.append(0)
        # you only need to calculate 4 out of 8 axes products. The rest will be convered by some other number
        # below rows same column
        if(row < 17):
            tempProducts.append(grid[row][column] * grid[row + 1][column] * grid[row + 2][column] * grid[row + 3][column])
        # right columns  
        if(column < 17):
            tempProducts.append(grid[row][column] * grid[row][column + 1] * grid[row][column + 2] * grid[row][column + 3])
        # right below diagonal
        if(row < 17 and column <17):
            tempProducts.append(grid[row][column] * grid[row + 1][column + 1] * grid[row + 2][column + 2] * grid[row + 3][column + 3])
        # above left diagonal
        if(row > 2 and column < 17):
            tempProducts.append(grid[row][column] * grid[row - 1][column + 1] * grid[row - 2][column + 2] * grid[row - 3][column + 3])
        # only append max of this number
        products.append(max(tempProducts))
print(max(products))
