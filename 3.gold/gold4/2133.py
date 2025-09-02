n = int(input())

tile = [0]*(n+1)
if len(tile) > 2:
    tile[0] = 1
    tile[2] = 3
    special = 0
    for i in range(4,n+1,2):
        tile[i] = tile[i-2] * 3
        for j in range(4,i+1,2):
            tile[i] += tile[i-j] * 2
if n % 2 == 0:
    print(tile[n])
else :
    print(0)