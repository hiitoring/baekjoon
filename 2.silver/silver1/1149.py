n = int(input())
house = list(list(map(int,input().split()))for _ in range(n))
answerdp = list([1000002] * 3 for _ in range(n))
answerdp[0][0] = house[0][0]
answerdp[0][1] = house[0][1]
answerdp[0][2] = house[0][2]
for i in range(n):
    for j in range(3):
        for k in range(3):
            if j != k:
                answerdp[i][k] = min(answerdp[i][k],answerdp[i-1][j] + house[i][k])
print(min(answerdp[-1]))