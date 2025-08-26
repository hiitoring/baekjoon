n = int(input())
numli = list(map(int,input().split()))
numcnt = [1] * n

for i in range(n):
    for j in range(i+1,n):
        if numli[i] > numli[j]:
            numcnt[j] = max(numcnt[j],numcnt[i] + 1)
print(max(numcnt))