num1, num2 = map(int, input().split())
arr = []

for i in range(1,num1+1):
    if num1 % i == 0:
        arr.append(i)

if len(arr) < num2: #이 조건을 꼭 넣어줘야함
    print(0)
else:
    print(arr[num2-1])