n1 = int(input())
#n1_arr = list(map(int,input().split()))
n1_arr = set(map(int,input().split()))

n2 = int(input())
n2_arr = list(map(int,input().split()))
result_arr = [0 for i in range(0,n2)]
result = []

for i in n2_arr:
    n = set(n2_arr)

    if len(n1_arr & n) == 1:
        result.append(1)
    else:
        result.append(0)

print(result)

'''시간 초과
n1 = int(input())
n1_arr = list(map(int,input().split()))
n2 = int(input())
n2_arr = list(map(int,input().split()))
result_arr = [0 for i in range(0,n2)]

for i in range(0,n1):
    for j in range(0,n2):
        if n1_arr[i] == n2_arr[j]:
            result_arr[j] = 1

for i in result_arr:
    print(i, end= ' ')
'''