n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
num_arr = []
combination_arr = []

for i in range(n):
    num_arr.append(i)


result = []
def combinations(n, new_arr, arr, c):
    if len(new_arr) == n//2:
        #print(new_arr)
        sum1 = 0
        sum2 = 0

        for i in new_arr:
            for j in new_arr:
                sum1 += s[i][j]
                sum2 += s[n - i - 1][n - j - 1]
        result.append(abs(sum1-sum2))
        #combination_arr.append(new_arr)
        return

    for i in range(c,len(arr)):
        combinations(n, new_arr+[arr[i]], arr, i+1)

combinations(n, [], num_arr, 0)
print(combination_arr)
print(min(result))
#print(combination_arr)
#combination_arr = combination_arr[0:(len(combination_arr)//2)]

'''for i in range(len(combination_arr)):
    sum1=0
    sum2=0
    for j in combination_arr[i]:
        for k in combination_arr[i]:
            sum1+=s[j][k]
            sum2+=s[n-j-1][n-k-1]
    result.append(abs(sum1-sum2))

print(result)'''

#combinations(2, [], combination_arr[0], 0)
#print(combination_arr)

'''for i in combination_arr:
    final_combination = []
    sum1 = 0
    sum2 = 0

    for j in range(len(i)):  # final_combination 계산 부분 수정
        final_combination.append(combinations(2, [], i, 0)[j])

    print(final_combination)

    for j in range(len(final_combination)):
        sum1 += s[final_combination[j][0]][final_combination[j][1]]
        sum2 += s[n-final_combination[j][0]-1][n-final_combination[j][1]-1]

    result.append(abs(sum2-sum1))
    #print(combination_arr)

print(min(result))'''

'''import sys
n = int(sys.stdin.readline())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
visit = [ False for _ in range(n) ] #1
min_value = sys.maxsize #2

def backTracking(depth, idx): #3
    global min_value
    if depth == n // 2: #4
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]: #5
                    power1 += graph[i][j]
                elif not visit[i] and not visit[j]: #6
                    power2 += graph[i][j]
        min_value = min(min_value, abs(power1-power2)) #7
        return

    for i in range(idx, n): #8
        if not visit[i]:
            visit[i] = True
            backTracking(depth+1, i+1) #9
            visit[i] = False
backTracking(0, 0)
print(min_value) '''

#1 : 1차원으로 방문 리스트 생성

#2 : 최소값을 갱신할 변수 생성

#3 : 깊이를 나타내는 변수와 인덱스 변수를 인자로 받아줌

#4 : n은 늘 짝수로 주어진다고 했다. 주어진 수의 절반이 한 팀으로 선택되었을때 가지치기 시작

#5 : True의 값을 가지는 팀을 스타트팀이라 할때 스타트 팀의 능력치를 모두 power1에 더하고

#6 : 나머지 절반 False의 값을 가지는 팀을 링크팀이라 할때 링크 팀의 능력치를 모두 power2에 더한다.

#7 : 2중 for문이 끝났을때 그 둘의 차이의 절댓값이 변수보다 작으면 변수 갱신

#8 : #4의 조건에 걸리기 전(스타트 팀을 완성하지 못했을때) 백트래킹 실시

#9 : 깊이 +1, 같은 번호 중복을 막기위한 idx+1로 재귀호출