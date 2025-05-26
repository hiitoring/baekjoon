from collections import deque
def popsuf(x):
    x.popleft()
    x.append(x[0])
    x.popleft() 

deck = deque()
n = int(input())
for i in range(n):
    deck.append(i+1)
while len(deck) > 1:
    popsuf(deck)
print(deck[0])