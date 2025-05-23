n, m = map(int,input().split()) #이진 탐색 이용
nlist = list(sorted(input()for _ in range(n)))
nlist.sort()
mlist = list(sorted(input()for _ in range(m)))
count=0
for i in range(m):
    left, right = 0, len(nlist)-1
    while left <= right:
        mid = (left + right) // 2
        if nlist[mid] == mlist[i]:
            count += 1
            break
        elif nlist[mid] < mlist[i]:
            left = mid + 1
        else:
            right = mid - 1
print(count)

        