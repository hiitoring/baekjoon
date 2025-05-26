from collections import deque
import ast
import sys

t = int(sys.stdin.readline())
deck = deque()
strdeck = deque()
for _ in range(t):
    reversed = False
    error = False
    comm = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    strdeck = sys.stdin.readline()
    deck = deque(ast.literal_eval(strdeck))
    for i in comm:
        if i == "R":
            reversed = not reversed
        elif i == "D":
            if not deck:
                print("error")
                error = True
                break
            if reversed:
                deck.pop()
            else:
                deck.popleft()               
    if not error:
        if reversed:
            deck.reverse()
        print("[" + ",".join(map(str,deck)) + "]")
   
        
