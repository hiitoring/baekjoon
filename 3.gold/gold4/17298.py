t = int(input())
nge = list(map(int,input().split()))
answer = [-1] * t
stack = []
for i in range(t):
    while stack and nge[stack[-1]] < nge[i]:
        idx = stack.pop()
        answer[idx] = nge[i]
    stack.append(i)
print(*answer)
    