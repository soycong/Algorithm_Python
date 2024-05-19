n = int(input())
nums = list(map(int, input().split()))
operator =  list(map(int, input().split()))

operator_arr=[]
permutations_arr=[]

for i in range(len(operator)):
    for j in range(operator[i]):
        operator_arr.append(i)
print(operator_arr)

visited = [0] * len(operator_arr)  # visited도 전역으로 둬도 됨

def permutations(n, new_arr):
    global operator_arr
    global permutations_arr

    # 순서 상관 0, 중복 X
    if len(new_arr) == n:
        #print(new_arr)
        permutations_arr.append(new_arr)
        return

    for i in range(len(operator_arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, new_arr + [operator_arr[i]])
            visited[i] = 0


permutations(len(operator_arr), [])
#print(permutations_arr)

result_arr = []
for i in range(len(permutations_arr)):
    result = nums[0]

    for j in range(1, len(nums)):
        if permutations_arr[i][j-1] == 0:
            result+=nums[j]
        elif permutations_arr[i][j-1] == 1:
            result -= nums[j]
        elif permutations_arr[i][j-1] == 2:
            result *= nums[j]
        elif permutations_arr[i][j-1] == 3:
            result /= nums[j]

    result_arr.append(result)

print(max(result_arr))
print(min(result_arr))