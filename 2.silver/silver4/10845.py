from collections import deque
import sys

def push(x):
    queue.append(x)
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

queue = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    comm = sys.stdin.readline().split()
    if len(comm) == 2:
        push(comm[1])
    elif comm[0] == "pop":
        pop(queue)
    elif comm[0] == "size":
        size(queue)
    elif comm[0] == "empty":
        empty(queue)
    elif comm[0] == "front":
        front(queue)
    elif comm[0] == "back":
        back(queue)