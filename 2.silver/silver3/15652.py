def backtrack(start,path):
    if len(path) == m:
            print(*path)
            return

    for i in range(start, n+1):
        path.append(i)
        backtrack(i,path)
        path.pop()
path = []
n, m = map(int,input().split())
backtrack(1,path)