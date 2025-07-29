n = int(input())
answer = [1] * 10
answer[0] = 0
support = [0] * 10
for i in range(n-1):
    for j in range(10):
        if j == 0:
            support[j] = answer[j+1]
        elif j == 9:
            support[j] = answer[j-1]
        else:
            support[j] = answer[j-1] + answer[j+1]
    for k in range(10):
        answer[k] = support[k]
print(sum(answer)%1000000000)