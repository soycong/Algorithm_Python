''' 시간 초과
n = int(input())
n_arr = list(map(int, input().split()))

n_set = set(n_arr)
n_set = sorted(n_set)

for i in n_arr:
    for j in range(0, len(n_set)):
        if i == n_set[j]:
            print(j)
'''

n = int(input())
n_arr = list(map(int, input().split()))

n_set = set(n_arr)
n_set = sorted(n_set)

n_dic = {n_set[i]: i for i in range(0, len(n_set))}

for i in n_arr:
    print(n_dic[i])