import sys
n,m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
prefix = [0]* (n+1)
for i in range(len(nums)):
    prefix[i+1] = prefix[i] + nums[i]
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    sum = prefix[y] - prefix[x-1]
    print(sum)