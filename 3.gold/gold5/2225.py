n , k = map(int,input().split())
hapbun = list([0]*(n+1) for _ in range(k+1))
for i in range(n+1):
    hapbun[1][i] = 1
for j in range(2,k+1):
    for N in range(n+1):
        if N == 0:
            hapbun[j][N] = 1
        else:
            hapbun[j][N] = (hapbun[j-1][N] + hapbun[j][N-1]) % 1000000000
print(hapbun[k][n])
