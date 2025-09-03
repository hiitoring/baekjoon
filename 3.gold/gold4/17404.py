n = int(input())
RGBst = [list(map(int,input().split()))for _ in range(n)]
answer = [[1000] * 3 for _ in range(n)]
start = [[0] * 3 for _ in range(n)]
start[0][0] = 1
start[0][1] = 2
start[0][2] = 3
answer[0][0] = RGBst[0][0]
answer[0][1] = RGBst[0][1]
answer[0][2] = RGBst[0][2]
for i in range(1,n):
    for j in range(3):
        for k in range(3):
            if j != k :
                if answer[i][k] > RGBst[i-1][j]+RGBst[i][k]:
                    answer[i][k] = answer[i-1][j]+RGBst[i][k]
                    start[i][k] = start[i-1][j]
print(answer)
print(start)


