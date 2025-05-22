m = int(input())
score = list(map(int,input().split()))
m_score = max(score)

for i in range(m):
    score[i] = score[i]/m_score*100

print(sum(score)/m)