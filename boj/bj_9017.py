testcase = int(input())  # 테스트 케이스 개수

for _ in range(0, testcase):
    dataNum = int(input())  # 입력 데이터의 개수
    data = list(map(int, input().split()))  # 테케 별 팀 점수

    # 각 숫자의 등장 횟수를 세는 딕셔너리 생성
    count_dict = {}
    for num in data:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # 등장 횟수가 5개 초과인 숫자만 필터링하여 새로운 배열 생성
    filtered_data = [num for num in data if count_dict[num] > 5]

    # 팀 별 점수를 저장할 배열
    data_arr = [[] for _ in range(max(filtered_data) + 1)]

    # 각 팀 별 점수 저장
    for i in range(1, max(filtered_data) + 1):
        for index, value in enumerate(filtered_data):
            if i == value:
                data_arr[i].append(index)

    # 각 팀의 4위까지의 합을 저장할 배열
    total = [float('inf')] * (max(filtered_data) + 1)

    # 한 팀에 6명인 조의 1~4등까지의 합
    for i in range(1, max(filtered_data) + 1):
        if sum(data_arr[i][0:4]) > 0:  # 최솟값 0 제외
            total[i] = sum(data_arr[i][0:4])

    total_min = min(total)  # 최소값 (1등)을 저장
    min_index = []  # 동점자를 저장할 배열

    # 1~4등까지의 합이 가장 작은 팀을 저장
    for index, value in enumerate(total):
        if value == total_min:
            min_index.append(index)

    equalizer = float('inf')  # 동점자
    winner = None  # 우승

    # 동점자가 있을 경우, 5번째 선수의 점수가 더 작은 팀이 우승
    for i in min_index:
        if data_arr[i][4] < equalizer:
            equalizer = data_arr[i][4]
            winner = i
    print(winner)