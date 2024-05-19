#t = int(input())
n = int(input())
#ingredients = [list(map(int,input().split())) for _ in range(n)]
combinations_arr = []

for i in range(n):
    combinations_arr.append(i)

#1 음식끼리의 조합
#arr = [1, 2, 3, 4]

# 현재 인덱스 +1 만큼을 매개변수로 계속 넘겨주어야함
# 순서가 상관없고 중복 불가이기 때문에 현재 인덱스보다 같거나 작은 인덱스는 볼 필요가 없기 때문

arr_new = []
def combinations(n, new_arr, c):
    # 순서 상관 X, 중복 X
    if len(new_arr) == n:
        #print(new_arr)
        arr_new.append(new_arr)
        return
    for i in range(c, len(combinations_arr)):
        combinations(n, new_arr + [combinations_arr[i]], i + 1)

product_arr = []
#arr = [1, 2, 3, 4]
def product(arr, n, new_arr):
    #global arr
    # 순서 상관 0, 중복 0
    if len(new_arr) == n:
        #print(new_arr)
        product_arr.append(new_arr)
        return
    for i in range(len(arr)):
        product(arr, n, new_arr + [arr[i]])

def permutations(n, new_arr):
    global arr
    # 순서 상관 0, 중복 X
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            visited[i] = 0


combinations(n/2, [], 0)
print(arr_new)

for i in arr_new:
    arr = i
    visited = [0] * len(arr)  # visited도 전역으로 둬도 됨
    permutations(2, [])