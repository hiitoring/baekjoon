t = int(input())
nums = map(int,input().split())
nums = list(nums)
count = 0
for i in range(t):
    flag = False
    for j in range(nums[i]-1,1,-1):
        if nums[i] % j == 0:
            flag = True
            break
    if flag == False and nums[i] != 1:
        count += 1
print(count)

