n_arr = []

for _ in range(0,3):
    n = int(input())
    n_arr.append(n)

n_set = set(n_arr)

if sum(n_arr) == 180:
    if len(n_set) == 1:
        print("Equilateral")
    elif len(n_set) == 2:
        print("Isosceles")
    elif len(n_set) == 3:
        print("Scalene")
else:
    print("Error")
