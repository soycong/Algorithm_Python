n, m = map(int, input().split())
data = list(map(int, input().split()) for _ in range(n))
move = []

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(m):
    movement = list(map(int, input().split()))
    move.append([movement[0]-1,movement[1]])

cloud = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

#---

# 입력 받기
n, m = map(int, input().split())  # n과 m을 입력 받음
data = [list(map(int, input().split())) for _ in range(n)]  # n개의 줄에 각각 m개의 수를 입력받아 이차원 리스트 data에 저장

# 구름 초기 위치 설정
cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]  # 초기 구름 위치 설정

# 이동 방향 설정
dx = [0, -1, -1, -1, 0, 1, 1, 1]  # x 방향 이동
dy = [-1, -1, 0, 1, 1, 1, 0, -1]  # y 방향 이동

# 구름 이동 정보 입력 받기
move = []  # 구름 이동 정보 저장할 리스트 초기화
for i in range(m):
    temp = list(map(int, input().split()))  # 사용자로부터 이동 정보 입력 받음
    move.append([temp[0] - 1, temp[1]])  # 이동 정보를 리스트로 저장 (인덱스 조정)

# 각 단계 수행
for i in range(m):  # m번 반복하면서 각 단계 수행
    # 1단계: 구름 이동
    moving = move[i]  # 현재 이동 정보 가져오기
    next_cloud = []  # 다음 구름 위치를 저장할 리스트 초기화
    for c in cloud:  # 현재 구름 위치마다 이동 처리
        x = c[0]  # 현재 구름의 x 좌표
        y = c[1]  # 현재 구름의 y 좌표
        d, s = moving[0], moving[1]  # 이동 방향과 거리 가져오기
        nx = (n + x + dx[d] * s) % n  # x 좌표 이동 후 경계 처리
        ny = (n + y + dy[d] * s) % n  # y 좌표 이동 후 경계 처리
        next_cloud.append([nx, ny])  # 다음 구름 위치 추가

    # 2단계: 물 복사 마법
    visited = [[False] * n for _ in range(n)]  # 방문 여부를 저장할 이차원 리스트 초기화
    for drop in next_cloud:  # 다음 구름 위치마다 물의 양 증가 및 방문 처리
        x = drop[0]  # 현재 위치의 x 좌표
        y = drop[1]  # 현재 위치의 y 좌표
        data[x][y] += 1  # 물의 양 증가
        visited[x][y] = True  # 방문 처리

    # 3단계: 구름 생성
    cloud = []  # 구름 위치를 초기화

    # 4단계: 대각선 방향 물 복사
    cx = [-1, -1, 1, 1]  # 대각선 방향 x 좌표 이동
    cy = [-1, 1, -1, 1]  # 대각선 방향 y 좌표 이동
    for j in next_cloud:  # 다음 구름 위치마다 대각선 방향의 물 양을 구하여 더함
        x = j[0]  # 현재 위치의 x 좌표
        y = j[1]  # 현재 위치의 y 좌표
        count = 0  # 대각선 방향의 물 양 초기화
        for k in range(4):  # 대각선 방향마다 물 양을 구하여 더함
            nx = x + cx[k]  # 대각선 방향의 x 좌표
            ny = y + cy[k]  # 대각선 방향의 y 좌표
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] >= 1:  # 범위 확인 후 물의 양 더함
                count += 1  # 물의 양 더함
        data[x][y] += count  # 현재 위치의 물의 양을 더함

    # 5단계: 구름 생성
    for j in range(n):  # 전체 행을 반복하면서
        for k in range(n):  # 전체 열을 반복하면서
            if data[j][k] >= 2 and visited[j][k] == False:  # 물의 양이 2 이상이고 방문하지 않았다면
                data[j][k] -= 2  # 물의 양을 2 줄이고
                cloud.append([j, k])  # 구름 추가

# 결과 출력
result = 0  # 결과를 저장할 변수 초기화
for i in range(n):  # 전체 행을 반복하면서
    result += sum(data[i])  # 각 행의 물의 양을 더하여 결과에 추가
print(result)  # 결과 출력

