S = input()
answer = []
for i in range(len(S)):
    answer.append(S[i:len(S)+1])
answer.sort()
for j in answer:
    print(j)
