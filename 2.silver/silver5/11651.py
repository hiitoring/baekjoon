n = int(input())
pointli = []
for _ in range(n):
    a, b = map(int,input().split())
    pointli.append((a,b))
pointli.sort(key=lambda x: (x[1],x[0]))
for i in range(n):
    print(*pointli[i])