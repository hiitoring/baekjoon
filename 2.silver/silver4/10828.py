from collections import deque
import sys

def push(x):
    stack.append(x)
def pop(x):
    if len(x) == 0 :
        return print(-1)
    else:
        return print(x.pop())
def size(x):
    return print(len(x))
def empty(x):
    if len(x) == 0:
       return print(1)
    else:
       return print(0)
def top(x):
    if len(x) == 0:
       return print(-1)
    else:
       return print(x[-1])

stack = []
n = int(sys.stdin.readline())
for _ in range(n):
    comm = sys.stdin.readline().split()
    if len(comm) == 2:
        push(comm[1])
    elif comm[0] == "pop":
        pop(stack)
    elif comm[0] == "size":
        size(stack)
    elif comm[0] == "empty":
        empty(stack)
    elif comm[0] == "top":
        top(stack)
