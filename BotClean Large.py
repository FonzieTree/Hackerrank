# problem from https://www.hackerrank.com/challenges/botcleanlarge
def next_move(posx, posy, dimx, dimy, board):
    out = []
    for x in range(dimx):
        for y in range(dimy):
            if board[x][y] == 'd':
                out.append([x, y])
    index = 0
    for k in range(len(out)):
        if abs(out[k][0]- posx) + abs(out[k][1] - posy) < abs(out[index][0] - posx) + abs(out[index][1] - posy):
            index = k
    x = out[index][0]
    y = out[index][1]
    if x == posx and y == posy:
        print("CLEAN")
    elif x > posx:
        print("DOWN")
    elif x < posx:
        print("UP")
    else:
        if y > posy:
            print("RIGHT")
        else:
            print("LEFT")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
