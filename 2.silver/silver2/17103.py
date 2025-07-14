t= int(input())
sosu = [True] * 1000001
sosu[0] = True
sosu[1] = True

for i in range(2,int(len(sosu)**0.5+1)):
    for j in range(i*i,len(sosu),i):
        if sosu[j]:
            sosu[j] = False

for _ in range(t):
    n = int(input())
    count=0
    for j in range(2,n//2+1):
        if sosu[j] and sosu[n-j]:
            if j+(n-j) == n:
              count += 1
    print(count)


