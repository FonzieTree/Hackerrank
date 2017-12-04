# problem from https://www.hackerrank.com/challenges/botclean
#!/usr/bin/python
# Head ends here
def next_move(posr, posc, board):
    out = []
    for x in range(5):
        for y in range(5):
            if board[x][y] == 'd':
                out.append([x, y])
    index = 0
    for k in range(len(out)):
        if abs(out[k][0]- posr) + abs(out[k][1] - posc) < abs(out[index][0] - posr) + abs(out[index][1] - posc):
            index = k
    x = out[index][0]
    y = out[index][1]
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

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
