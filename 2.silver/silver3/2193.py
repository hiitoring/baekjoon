n = int(input())
chins = [0] * (n+1)
chins[1] = 1
for i in range(2,n+1):
    chins[i] = chins[i-2] + chins[i-1]
print(chins[n])
