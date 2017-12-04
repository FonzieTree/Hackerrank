# problem from https://www.hackerrank.com/challenges/botcleanr
#!/bin/python3
def nextMove(posr, posc, board):
    out = []
    for x in range(5):
        for y in range(5):
            if board[x][y] == 'd':
                out.append(x)
                out.append(y)
    x = out[0]
    y = out[1]
    if x == posr and y == posc:
        print("CLEAN")
    elif x > posr:
        print("DOWN")
    elif x < posr:
        print("UP")
    else:
        if y > posc:
            print("RIGHT")
        else:
            print("LEFT")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
