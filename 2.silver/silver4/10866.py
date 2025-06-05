import sys
from collections import deque
nums = deque()
def push_front(X):
    nums.append(X)
    nums.rotate(1)
def push_back(X):
    nums.append(X)
def pop_front():
    if nums:
        return print(nums.popleft())
    else:
       return print(-1)
def pop_back():
    if nums:
        return print(nums.pop())
    else:
        return print(-1)
def size():
    return print(len(nums))
def empty():
    if nums:
       return print(0)
    else:
       return print(1)
def front():
    if nums:
       return print(nums[0])
    else:
      return print(-1)
def back():
    if nums:
       return print(nums[-1])
    else:
       return print(-1)
n = int(sys.stdin.readline())
for _ in range(n):
    comm = sys.stdin.readline().split()
    if len(comm) == 2:
        if comm[0] == "push_front":
            push_front(comm[1])
        if comm[0] == "push_back":
            push_back(comm[1])
    else:
        if comm[0] == "pop_front":
            pop_front()
        if comm[0] == "pop_back":
            pop_back()
        if comm[0] == "size":
            size()
        if comm[0] == "empty":
            empty()
        if comm[0] == "front":
            front() 
        if comm[0] == "back":
            back()       