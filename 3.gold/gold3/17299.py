from collections import Counter
import sys
n = int(sys.stdin.readline())
ngf = list(map(int,sys.stdin.readline().split()))
answer = [-1] * n
miri = Counter(ngf)
stack = []
for i in range(n):
  while stack and miri[ngf[stack[-1]]] < miri[ngf[i]]:
    idx = stack.pop()
    answer[idx] = ngf[i]
  stack.append(i)
print(*answer)