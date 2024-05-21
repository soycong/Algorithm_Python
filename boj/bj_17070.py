def root(x, y, state):
    global cnt
    if x == n - 1 and y == n - 1:
        cnt += 1
        return

    if state == 0:
        if board[x + 1][y] == 1 or x == n-1:
            return

        elif board[x + 1][y] == 0:
            root(x + 1, y, 0)

        elif board[x + 1][y] == 0 and board[x][y + 1] == 0 and board[x + 1][y + 1] == 0:
            root(x + 1, y + 1, 2)

    elif state == 1:
        if board[x][y + 1] == 1 or y == n-1:
            return

        elif board[x][y + 1] == 0:
            root(x, y + 1, 1)

        elif board[x + 1][y] == 0 and board[x][y + 1] == 0 and board[x + 1][y + 1] == 0:
            root(x + 1, y + 1, 2)

    else:
        if board[x + 1][y + 1] == 1 and board[x][y + 1] == 1 and board[x + 1][y] == 1:
            return

        elif board[x + 1][y] == 0:
            root(x + 1, y, 0)

        elif board[x][y + 1] == 0:
            root(x, y + 1, 1)

        elif board[x + 1][y] == 0 and board[x][y + 1] == 0 and board[x + 1][y + 1] == 0:
            root(x + 1, y + 1, 2)

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

dx = [1,0,1]
dy = [0,1,1]

cnt = 0
state = 0
x = 0
y = 1

root(x,y,state)

print(cnt)
