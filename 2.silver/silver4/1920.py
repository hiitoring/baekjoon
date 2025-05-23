n = int(input())   # 이진 탐색법 사용
ali = list(map(int,input().split()))
m = int(input())
bli = list(map(int,input().split()))
ali.sort()
for i in range(m):
    left, right = 0,len(ali)-1
    found = 0
    while left <= right:
        mid = (left + right) // 2
        if ali[mid] == bli[i]:
            found = 1
            break
        elif ali[mid] < bli[i]:
            left = mid + 1
        else:
            right = mid - 1
    print(found) 