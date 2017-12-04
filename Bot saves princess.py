#!/usr/bin/python
# problem from https://www.hackerrank.com/challenges/saveprincess/problem
import math
def displayPathtoPrincess(n,grid):
    k = int(math.floor(m/2))
    if grid[0][0] == 'p':
        for i in range(k):
            print('UP')
            print('LEFT')
    elif grid[0][m-1] == 'p':
        for i in range(k):
            print('UP')
            print('RIGHT')
    elif grid[m-1][0] == 'p':
        for i in range(k):
            print('DOWN')
            print('LEFT')
    elif grid[m-1][m-1] == 'p':
        for i in range(k):
            print('DOWN')
            print('RIGHT')
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())
displayPathtoPrincess(m,grid)
