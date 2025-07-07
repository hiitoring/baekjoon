def gcd(x,y):
    while y:
        x,y = y , x%y
    return x

n,s = map(int,input().split())
bro = list(map(int,input().split()))
for i in range(n):
    if s < bro[i]:
        bro[i] = bro[i] - s
    else:
        bro[i] = s - bro[i]
GCD = bro[0]        
for j in range(1,n):
    GCD = gcd(GCD,bro[j])
print(GCD)