#시간 초과
'''
n = int(input())
sum = 0

for i in range(0,n):
    sum += 2*i

print(sum)

#겹치는 부분을 생각 못함..
n = int(input())
sum = 0

if n == 1:
    sum = 0
elif n == 2:
    sum = 3
else:
    sum = n * (n-1)

print(4*n-sum)
'''

n = int(input())
print(4*n)
