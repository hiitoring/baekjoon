a = int(input())
numli = list(map(int,input().split()))
answer = [1] * a
for i in range(a):
    for j in range(i+1,a):
        if numli[i] < numli[j]:
            answer[j] = max(answer[j],answer[i] + 1)

print(max(answer))
    