n = int(input())
numli = list(map(int,input().split()))
toleft = [0] * n
toright = [0] * n
toleft[0] = numli[0]
toright[n-1] = numli[n-1]

for i in range(1,n):
    rev = n-i-1
    toleft[i] = max(toleft[i-1] + numli[i], numli[i])
    toright[rev] = max(toright[rev+1] + numli[rev], numli[rev]) 
    print(toleft)
    print(toright)

minusmax = (max(toleft))
for j in range(1,n-1):
    minusmax = max(toleft[j-1]+toright[j+1],minusmax)
print(minusmax)