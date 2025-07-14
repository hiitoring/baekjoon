n,b = map(int,input().split())
rst =''
while n > 0:
    n,y = divmod(n,b)
    if y >= 10:
        y = chr(y+55)
    rst = str(y) + rst
print(rst)   
