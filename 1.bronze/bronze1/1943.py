import sys
t = int(sys.stdin.readline())
answer = 1
for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    i = min(a,b)
    for i in range(i,0,-1):
        an = a % i
        bn = b % i
        if an == 0 and bn == 0:
            a = a // i
            b = b // i
            print(a*b*i)
            break

        