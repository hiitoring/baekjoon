n = int(input())
zegop = [n] * (n+1)
zegop[0] = 0
for i in range(1,n+1):
    for j in range(1,int(i**0.5)+1):
        zegop[i] = min(zegop[i],zegop[i-j*j]+1)
print(zegop[n])

        