# problem from https://www.hackerrank.com/challenges/saveprincess2/problem
def nextMove(n,r,c,grid):
    
    if a < r:
        return('UP')
    elif a > r:
        return('DOWN')
    else:
        if b < c:
            return('LEFT')
        else:
            return('RIGHT')

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []

for i in range(0, n):
    grid.append(input())
    if 'p' in grid[i]:
        a = i
b=grid[a].index('p')
print(nextMove(n,r,c,grid))
