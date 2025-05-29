from collections import deque
import sys
sys.setrecursionlimit(1000000)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if bat[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
t= int(input())
for _ in range(t):
    m, n, k = map(int,input().split())
    count = 0
    bat = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        bat[b][a] = 1
    for i in range(m):
        for j in range(n):
            if bat[j][i] == 1 and not visited[j][i]:
                bfs(j,i)
                count +=1
    print(count)