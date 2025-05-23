from bisect import bisect_left, bisect_right #
#bisect 사용 버전
n, m = map(int,input().split())
nlist = list(sorted(input()for _ in range(n)))
nlist.sort()
mlist = list(sorted(input()for _ in range(m)))
count = 0
for i in range(m):
    x = mlist[i]
    left = bisect_left(nlist,x)
    right = bisect_right(nlist,x)
    count += right - left
print(count)