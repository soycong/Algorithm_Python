n = int(input())
cowArr = [2] * 10

count = 0

for i in range(0,n):
    cowNum, movement= map(int, input().split())

    if cowArr[cowNum-1] == 2:
        cowArr[cowNum - 1] = movement

    if cowArr[cowNum-1] != 2 and cowArr[cowNum-1] != movement:
        count+=1
        cowArr[cowNum - 1] = movement

print(count)