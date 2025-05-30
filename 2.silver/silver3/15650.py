def backtrack(path):
    if len(path) == m and path == sorted(path):
        print(*path)
        return
    for i in range(1,n+1):
        if not visited[i]:
            path.append(i)
            visited[i] = True
            backtrack(path)
            path.pop()
            visited[i] = False
path = []
n, m = map(int,input().split())
visited = [False] * (n+1)
backtrack(path)