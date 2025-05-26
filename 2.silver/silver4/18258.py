from collections import deque
import sys

def push(x):
    commli.append(x)
def pop(x):
    if len(x) == 0:
        return print(-1)
    else:     
        return print(x.popleft())
def size(x):
    return print(len(x))
def empty(x):
    if len(x) == 0:
        return print(1)
    else:
        return print(0)
def front(x):
    if len(x) == 0:
        return print(-1)
    else:
        return print(x[0])
def back(x):
    if len(x) == 0:
        return print(-1)
    else:
        return print(x[-1])

n = int(sys.stdin.readline())
commli = deque()
for _ in range(n):
    comm = sys.stdin.readline().split()
    if len(comm) == 2:
        push(comm[1])        
    elif comm[0] == "pop":
        pop(commli)
    elif comm[0] == "size":
        size(commli)
    elif comm[0] == "empty":
        empty(commli)
    elif comm[0] == "front":
        front(commli)
    elif comm[0] == "back":
        back(commli)