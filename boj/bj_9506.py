while True:
    num = int(input())
    arr = []
    sum = 0

    if num == -1:
        break

    for i in range(1, num):
        if num % i == 0:
            arr.append(i)

    for i in range(0,len(arr)):
        sum+=arr[i]

    if sum == num:
        print(str(num) + " = ", end="")
        for j in range(0, len(arr)):
            print(arr[j], end="")

            if j == len(arr) - 1:
                print("")
                break

            for _ in range(0, 1):
                print(" + ", end="")
    else:
        print(str(num) + " is NOT perfect.")