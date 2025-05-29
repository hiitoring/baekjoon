from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
allcount = []
allc = 0
def bfs(x,y):
    count = 1
    allcount.append(0)
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if town[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    town[nx][ny] = town[x][y] + 1
                    queue.append((nx,ny))
                    count += 1
    allcount[allc] = count


n = int(input())
town = [list(map(int,input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if town[i][j] == 1 and not visited[i][j]:
            bfs(i,j)
            allc +=1
allcount.sort()
print(len(allcount))
for i in allcount:
    print(i)
