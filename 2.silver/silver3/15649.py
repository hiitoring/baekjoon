def backtrack(path):
    if len(path) == m:
        print(*path)
        return
    for i in range(1, n+1):
        if i not in path:
            path.append(i)
            backtrack(path)
            path.pop()

path = []
n, m = map(int,input().split())
backtrack(path)