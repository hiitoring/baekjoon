from bisect import bisect_left, bisect_right

n = int(input())
num = list(map(int,(input().split())))
num.sort()
m = int(input())
gotnum = list(map(int,(input().split())))
count = []
for i in range(m):
    x = gotnum[i]
    value = bisect_right(num,x) - bisect_left(num,x)
    count.append(value)
print(*count)