n = int(input())
numli = list(map(int,input().split()))
answer = []
maxsum = 0

for k in range(n):
    answer.append(numli[k])
for i in range(n):
    for j in range(i+1,n):
        if numli[i] < numli[j]:
            answer[j] = max(answer[j],numli[j] + answer[i])
print(max(answer))