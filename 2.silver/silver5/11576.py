def dwnjin(x,y):
    while x > 0:
        x,na = divmod(x,y)
        bjin.append(na)
    bjin.reverse()
    return print(*bjin)

a,b = map(int,input().split())
t = int(input()) 
ajin = list(map(int,input().split()))
bjin = []
arst = 0

for i in ajin:
    t -= 1
    arst += i * (a ** t)

dwnjin(arst,b)
