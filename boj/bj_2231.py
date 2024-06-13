n = int(input())

for i in range(1, n+1):
    digit_sum = i + sum(map(int, str(i)))

    if digit_sum == n:
        print(i)
        break

    if i == n:
        print(0)
