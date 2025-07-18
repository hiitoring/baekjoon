n = int(input())
tile = [0] * (n+1)
tile[1] = 1
for i in range(2,n+1):
    if i == 2:
        tile[i] = 2
    else:
        tile[i] = tile[i-1] + tile[i-2]
print(tile[n]%10007)