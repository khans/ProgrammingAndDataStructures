#!/bin/python3

import sys

def getWays(n, c):
    # Complete this function
    comb = [0 for j in range(n+1)]
    comb[0] = 1
    for each in c:
        for j in range(n+1):
            if j >= each:            #if current value is greater than or equal to the denomination
                comb[j] += comb[j-each]
    print (comb[-1])
    return comb[-1]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
# https://www.youtube.com/watch?v=jaNZ83Q3QGc