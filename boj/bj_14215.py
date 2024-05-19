n_arr = list(map(int, input().split()))
n_arr.sort()


if n_arr[0] + n_arr[1] > n_arr[2]:
    print(sum(n_arr))

elif n_arr[0] + n_arr[1] - 1 <= n_arr[2]:
    print((n_arr[0] + n_arr[1])*2-1)

elif n_arr[1] <= n_arr[2]:
    print(n_arr[0] + (n_arr[1] * 2))

else:
    print(n_arr[0] * 3)
