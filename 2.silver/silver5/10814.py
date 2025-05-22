n = int(input())
list = []
for _ in range(n):
    a,b = input().split()
    list.append((int(a), b))
list.sort(key=lambda x: x[0])
for i in range(n):
    print(*list[i])
