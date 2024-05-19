n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(m):
    d, s = map(int, input().split())

    x = n // 2
    y = n // 2

    for i in range(s):
            x+=dx[d-1]
            y+=dy[d-1]
            board[x][y] = 0

# 회전 함수
# n//2+1 제외하고 0일 경우, rotation 진행
def rotation():


#4개 이상 폭발 함수
def explode():
    #4개 이상 -> 폭발 (0)으로 채우기
    #없으면 rotation

#A,B로 채우기 함수
def board_Reset():
    #1. 현재 보드에서 A그룹, B그룹 추출
    #2. x,y n//2 + 1 부터 채우기, 없는 곳은 0, 상어 위치도 0