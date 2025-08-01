n = int(input())
numli = list(map(int,input().split()))
supp = [0] * n
supp[0] = numli[0]
answer = numli[0]
for i in range(1,n):
    supp[i] = max(supp[i-1] + numli[i],numli[i])
    answer = max(answer,supp[i])
print(answer)