from collections import deque
import re
def Rev(x):
    x.reverse()
def dele(x):
    x.popleft()

t = int(input())
deck = deque()
for _ in range(t):
    comm = input()
    n = int(input())
    deck = input().strip("[]")
    deck = list(deck)
    while "," in deck:
        deck.remove(",")
    print(f"[{','.join(deck)}])
    