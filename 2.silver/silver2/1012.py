import sys
sys.setrecursionlimit(1000000)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny=  y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 1 and not visited[nx][ny]:
                 dfs(nx,ny)
        
t = int(input())
for _ in range(t):
    count = 0
    m,n,k = map(int,input().split())
    maze= [[0]*m for _ in range(n)]
    visited= [[False]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        maze[y][x] =  1
    for i in range(m):
        for j in range(n):
            if maze[j][i] == 1 and not visited[j][i]:
                dfs(j,i)
                count += 1
    print(count)
        
