def dae(a, b):
    while b:
        a,b = b, a%b
    return a
def so(a, b):
    return a*b // dae(a,b)

t= int(input())
for _ in range(t):
    a,b = map(int,input().split())
    print(so(a,b))