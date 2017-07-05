# -*- coding: utf-8 -*-
import sys


print('Dear user, please enter six row of six values in each, separated by a '
      'space, the values must be integers in the range from -9 to 9 inclusive.')
sand = []
# Create multidimensional array
for sand_i in range(6):
    sand_temp = list(map(int, input(' ').strip().split(' ')))
# Checking the entered values for compliance with the specified range
    for elem in sand_temp:
        if abs(elem) > 9:
            raise ValueError(' The entered number is outside the range from -9 to 9 inclusive!')
    sand.append(sand_temp)
BiggerSum = 0
# Scan array and find all 'hourglasses'
for i in range(len(sand)-2):
    for j in range(len(sand[0])-2):
        sum = sand[i][j] + sand[i][j+1] + sand[i][j+2] + sand[i+1][j+1] + sand[i+2][j] + sand[i+2][j+1] + sand[i+2][j+2]
# Compare of sum
        if BiggerSum < sum:
            BiggerSum = sum
print(' The biggest value sum of "hourglasses" is - '+str(BiggerSum))
