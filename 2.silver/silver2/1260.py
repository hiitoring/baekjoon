from collections import deque
graph = {}
def dfs(v):
    visited_dfs[v] = True
    print(v, end=" ")
    for i in sorted(graph[v]):
        if not visited_dfs[i]:
            dfs(i)
def bfs(v):
    visited_bfs[v] = True
    queue = deque([v])
    while queue:
        num = queue.popleft()
        print(num, end=" ")
        for i in sorted(graph[num]):
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)
n, m, v = map(int,input().split())
for i in range(n):
    graph[i+1] = []
for _ in range(m):
    poi, des = map(int,input().split())
    graph[poi].append(des)
    graph[des].append(poi)
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
dfs(v)
print("")
bfs(v)