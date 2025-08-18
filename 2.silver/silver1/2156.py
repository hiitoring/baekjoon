n = int(input())
wine = []
answer = list([0]*3 for _ in range(n))
for i in range(n):
    wine.append(int(input()))
answer[0][0] = 0
answer[0][1] = wine[0]
maxwine = wine[0]
for j in range(1,n):
    answer[j][0] = max(answer[j-1][0],answer[j-1][1],answer[j-1][2])
    answer[j][1] = wine[j] + answer[j-1][0]
    answer[j][2] = answer[j-1][1]+wine[j]
    maxwine = max(maxwine,max(answer[j]))
print(maxwine)