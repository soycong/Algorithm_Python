while(1):
    n_arr = list(map(int, input().split()))
    n_arr.sort()

    n_set = set(n_arr)

    if n_arr[0] + n_arr[1] > n_arr[2]:
        if len(n_set) == 3:
            print("Scalene")

        elif len(n_set) == 2:
            print("Isosceles")

        elif len(n_set) == 1 :
            print("Equilateral")

    else:
        if sum(n_arr) == 0:
            break

        else:
            print("Invalid")