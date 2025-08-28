n = int(input())
numli = list(map(int,input().split()))

climbup = [1] * n
climbdown = [1] * n
bitonic = [0] * n
maxbitonic = 1

for i in range(n):
    for j in range(i+1,n):
        if numli[i] < numli[j]:
            climbup[j] = max(climbup[i]+1,climbup[j])
        if  numli[n-1-i] < numli[n-1-j]:
            climbdown[n-1-j] = max(climbdown[n-1-i]+1,climbdown[n-1-j])

for k in range(n):
    bitonic[k] = climbup[k] + climbdown[k] - 1 
    maxbitonic = max(maxbitonic,bitonic[k])

print(maxbitonic)