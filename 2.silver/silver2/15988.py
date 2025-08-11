import sys
input = sys.stdin.readline
t = int(input())
ans = [0] * 1000001
ans[1]= 1
ans[2]= 2
ans[3]= 4
for i in range(4,1000001):
        ans[i] = (ans[i-1] + ans[i-2] + ans[i-3]) % 1000000009
for _ in range(t):
    n = int(input())
    print(ans[n] % 1000000009)
        
    