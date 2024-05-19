n, k = map(int,input().split())
arr = list(input())
new_arr = [[] for _ in range(12)]

for a in range(3):
    j = 0
    for b in range(4):
        for c in range(n//4):
            if j <= n-1:
                new_arr[a * 4 + b].append(arr[j])
            j+=1
    arr = [arr[-1]] + arr[:-1]

get_together = [''.join(sublist) for sublist in new_arr]
get_together = set(get_together)

result = []
for i in get_together:
    result.append(int(i, 16))

result.sort(reverse=True)
print("#", end = "")
print(n, end = " ")
print(result[k-1])

#print(result)
#print(result[k-1])
#print(arr)
#print(new_arr)
#print(rotation_arr)

'''arr = [['1', 'B', '3'], ['B', '3', 'B'], ['8', '1', 'F'], ['7', '5', 'E']]

# 각 하위 리스트를 하나의 문자열로 합치기
result = [''.join(sublist) for sublist in arr]

# 결과 출력
print(result)'''