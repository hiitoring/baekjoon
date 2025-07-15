n = int(input())
i = 2
answer = []
while n > 1:
    x,y = divmod(n,i)
    if y == 0:
        answer.append(i)
        i = 2
        n = x
    else:
        i += 1
answer.sort()
for j in answer:
    print(j)
    