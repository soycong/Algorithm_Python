nums = []
for i in range(0,5):
    n = int(input())
    nums.append(n)

nums.sort()
print(sum(nums)//5)
print(nums[2])