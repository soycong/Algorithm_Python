n = int(input())
n_arr = []
result = 0
result2=0

#1 시간 초과
for i in range(0, n-2):
    n_arr.append(i+1)

for i in range(n-2, 0, -1):
    result+=sum(n_arr)
    n_arr.remove(i)

#2 시간 초과
for i in range(1, n-1):
    for j in range(i, n-1):
        result2+=i

print(result)
print(result2)

#3
print(n*(n-1)*(n-2)//6) #이렇게 공식이 나옴
print(3)

