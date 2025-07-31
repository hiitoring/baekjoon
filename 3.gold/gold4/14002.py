n = int(input())
numli = list(map(int,input().split()))
supp = [1] * n
for i in range(n):
    for j in range(i+1,n):
        if numli[i] < numli[j]:
            supp[j] = max(supp[j],supp[i] + 1)
maxsupp = max(supp)
print(maxsupp)
maxidx = supp.index(maxsupp)
minus = 0
answer=[]
for k in range(maxidx,-1,-1):
    if supp[k] == maxsupp - minus:
        answer.append(numli[k])
        minus += 1
    if minus < 1:
        break
for o in range(len(answer)-1,-1,-1):
    print(answer[o],end=" ")

